import os
import django
import sys
import traceback
from datetime import datetime
from unittest.mock import MagicMock

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'grovix_backend.settings')
django.setup()

from inquiries.utils import send_email_to_customer, send_email_to_client

inquiry = MagicMock()
inquiry.inquiry_id = "TEST1234"
inquiry.name = "Test User"
inquiry.email = "test@example.com"
inquiry.phone = "1234567890"
inquiry.company = "Test Co"
inquiry.selected_plan = "Starter"
inquiry.message = "This is a test message"
inquiry.created_at = datetime.now()

try:
    print("Sending to customer")
    send_email_to_customer(inquiry)
except Exception as e:
    print(f"FAILED TO CUSTOMER:")
    traceback.print_exc()

try:
    print("Sending to client")
    send_email_to_client(inquiry)
except Exception as e:
    print(f"FAILED TO CLIENT:")
    traceback.print_exc()
