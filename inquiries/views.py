from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import Inquiry
from .forms import InquiryForm
from .utils import send_email_to_client, send_email_to_customer, update_excel_sheet
import json

def contact_view(request):
    """Handle contact form submission"""
    selected_plan = request.GET.get('plan', '')
    
    if request.method == 'POST':
        form = InquiryForm(request.POST)
        if form.is_valid():
            inquiry = form.save()
            
            # Send email to client (business) and confirmation to customer
            email_sent = send_email_to_client(inquiry)
            customer_email_sent = send_email_to_customer(inquiry)

            # Update Excel sheet
            excel_updated = update_excel_sheet(inquiry)

            return redirect('inquiry_success', inquiry_id=inquiry.inquiry_id)
    else:
        initial_data = {}
        if selected_plan:
            initial_data['selected_plan'] = selected_plan
        form = InquiryForm(initial=initial_data)
    
    return render(request, 'inquiries/contact.html', {
        'form': form,
        'selected_plan': selected_plan
    })

def inquiry_success(request, inquiry_id):
    """Display success page after inquiry submission"""
    try:
        inquiry = Inquiry.objects.get(inquiry_id=inquiry_id)
        return render(request, 'inquiries/success.html', {'inquiry': inquiry})
    except Inquiry.DoesNotExist:
        return redirect('contact')

@csrf_exempt
def api_submit_inquiry(request):
    """API endpoint for AJAX form submission"""
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            
            inquiry = Inquiry.objects.create(
                name=data.get('name'),
                email=data.get('email'),
                phone=data.get('phone'),
                company=data.get('company', ''),
                selected_plan=data.get('selected_plan'),
                message=data.get('message', '')
            )
            
            # Send notifications
            send_email_to_client(inquiry)
            send_email_to_customer(inquiry)
            update_excel_sheet(inquiry)
            
            return JsonResponse({
                'success': True,
                'inquiry_id': inquiry.inquiry_id,
                'message': 'Inquiry submitted successfully!'
            })
        except Exception as e:
            return JsonResponse({
                'success': False,
                'error': str(e)
            }, status=400)
    
    return JsonResponse({'error': 'Invalid request method'}, status=405)
