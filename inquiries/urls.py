from django.urls import path
from . import views

urlpatterns = [
    path('contact/', views.contact_view, name='contact'),
    path('success/<str:inquiry_id>/', views.inquiry_success, name='inquiry_success'),
    path('api/submit-inquiry/', views.api_submit_inquiry, name='api_submit_inquiry'),
]
