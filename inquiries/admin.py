from django.contrib import admin
from .models import Inquiry

@admin.register(Inquiry)
class InquiryAdmin(admin.ModelAdmin):
    list_display = ['inquiry_id', 'name', 'email', 'phone', 'selected_plan', 'created_at']
    list_filter = ['selected_plan', 'created_at']
    search_fields = ['inquiry_id', 'name', 'email', 'phone', 'company']
    readonly_fields = ['inquiry_id', 'created_at']
    ordering = ['-created_at']
    
    fieldsets = (
        ('Inquiry Information', {
            'fields': ('inquiry_id', 'created_at')
        }),
        ('Customer Details', {
            'fields': ('name', 'email', 'phone', 'company')
        }),
        ('Plan & Message', {
            'fields': ('selected_plan', 'message')
        }),
    )
