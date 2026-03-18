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

def _add_cors_headers(response):
    """Add CORS headers to any response."""
    response['Access-Control-Allow-Origin'] = 'https://grovixstudio-dusky.vercel.app'
    response['Access-Control-Allow-Methods'] = 'POST, OPTIONS'
    response['Access-Control-Allow-Headers'] = 'Content-Type'
    return response

@csrf_exempt
def api_submit_inquiry(request):
    """API endpoint for AJAX form submission"""
    # Handle CORS preflight
    if request.method == 'OPTIONS':
        response = JsonResponse({})
        response['Access-Control-Max-Age'] = '86400'
        return _add_cors_headers(response)

    if request.method != 'POST':
        return _add_cors_headers(
            JsonResponse({'error': 'Invalid request method'}, status=405)
        )

    # Wrap EVERYTHING in try/except to guarantee CORS headers on errors
    try:
        data = json.loads(request.body)
        
        inquiry = Inquiry.objects.create(
            name=data.get('name', ''),
            email=data.get('email', ''),
            phone=data.get('phone', ''),
            company=data.get('company', ''),
            selected_plan=data.get('selected_plan', ''),
            message=data.get('message', '')
        )
        
        # Send notifications - these should NEVER crash the request
        try:
            send_email_to_client(inquiry)
        except Exception as e:
            print(f"Email to client failed: {e}")
        
        try:
            send_email_to_customer(inquiry)
        except Exception as e:
            print(f"Email to customer failed: {e}")
        
        try:
            update_excel_sheet(inquiry)
        except Exception as e:
            print(f"Excel update failed: {e}")
        
        return _add_cors_headers(JsonResponse({
            'success': True,
            'inquiry_id': inquiry.inquiry_id,
            'message': 'Inquiry submitted successfully!'
        }))
    except Exception as e:
        import traceback
        traceback.print_exc()
        return _add_cors_headers(JsonResponse({
            'success': False,
            'error': str(e)
        }, status=400))
