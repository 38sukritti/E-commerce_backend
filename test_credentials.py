"""
Test Email and WhatsApp Configuration
Run this script to verify your credentials are working
"""

import os
import sys
from pathlib import Path

# Add the project directory to the Python path
BASE_DIR = Path(__file__).resolve().parent
sys.path.append(str(BASE_DIR))

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'grovix_backend.settings')
import django
django.setup()

from django.conf import settings
from django.core.mail import send_mail
from twilio.rest import Client

def test_email():
    """Test email configuration"""
    print("\n" + "="*50)
    print("TESTING EMAIL CONFIGURATION")
    print("="*50)
    
    print(f"\n📧 Email Settings:")
    print(f"   Host User: {settings.EMAIL_HOST_USER}")
    print(f"   Client Email: {settings.CLIENT_EMAIL}")
    print(f"   Password: {'*' * len(settings.EMAIL_HOST_PASSWORD) if settings.EMAIL_HOST_PASSWORD != 'your-gmail-app-password' else 'NOT CONFIGURED'}")
    
    if settings.EMAIL_HOST_USER == 'your-email@gmail.com':
        print("\n❌ Email NOT configured!")
        print("   Please edit .env file with your Gmail credentials")
        print("   See SETUP_CREDENTIALS.md for instructions")
        return False
    
    try:
        print("\n📤 Sending test email...")
        send_mail(
            subject='Test Email from Grovix Studio',
            message='This is a test email. If you receive this, your email configuration is working!',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[settings.CLIENT_EMAIL],
            fail_silently=False,
        )
        print("✅ Email sent successfully!")
        print(f"   Check inbox: {settings.CLIENT_EMAIL}")
        print("   (Also check spam folder)")
        return True
    except Exception as e:
        print(f"❌ Email failed: {str(e)}")
        print("\n💡 Common issues:")
        print("   - App password incorrect (should be 16 characters)")
        print("   - 2FA not enabled on Gmail")
        print("   - Email address incorrect")
        return False

def test_whatsapp():
    """Test WhatsApp configuration"""
    print("\n" + "="*50)
    print("TESTING WHATSAPP CONFIGURATION")
    print("="*50)
    
    print(f"\n💬 WhatsApp Settings:")
    print(f"   Account SID: {settings.TWILIO_ACCOUNT_SID[:10]}..." if settings.TWILIO_ACCOUNT_SID != 'your-twilio-account-sid' else "   Account SID: NOT CONFIGURED")
    print(f"   Auth Token: {'*' * 20 if settings.TWILIO_AUTH_TOKEN != 'your-twilio-auth-token' else 'NOT CONFIGURED'}")
    print(f"   WhatsApp Number: {settings.TWILIO_WHATSAPP_NUMBER}")
    
    if settings.TWILIO_ACCOUNT_SID == 'your-twilio-account-sid':
        print("\n❌ WhatsApp NOT configured!")
        print("   Please edit .env file with your Twilio credentials")
        print("   See SETUP_CREDENTIALS.md for instructions")
        return False
    
    # Ask for phone number
    print("\n📱 Enter your phone number to test WhatsApp:")
    print("   Format: +919876543210 (include country code)")
    phone = input("   Phone: ").strip()
    
    if not phone.startswith('+'):
        print("❌ Phone number must start with + and country code")
        return False
    
    try:
        print(f"\n📤 Sending test WhatsApp to {phone}...")
        client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
        
        message = client.messages.create(
            from_=f'whatsapp:{settings.TWILIO_WHATSAPP_NUMBER}',
            body='🎉 Test message from Grovix Studio! If you receive this, your WhatsApp configuration is working!',
            to=f'whatsapp:{phone}'
        )
        
        print(f"✅ WhatsApp sent successfully!")
        print(f"   Message SID: {message.sid}")
        print(f"   Check WhatsApp on: {phone}")
        return True
    except Exception as e:
        print(f"❌ WhatsApp failed: {str(e)}")
        print("\n💡 Common issues:")
        print("   - WhatsApp sandbox not joined")
        print("   - Phone number format incorrect")
        print("   - Twilio credentials incorrect")
        print("   - Twilio account balance insufficient")
        return False

def main():
    """Run all tests"""
    print("\n" + "="*50)
    print("GROVIX STUDIO - CREDENTIALS TEST")
    print("="*50)
    print("\nThis script will test your email and WhatsApp configuration")
    print("Make sure you've edited the .env file first!")
    
    input("\nPress Enter to start testing...")
    
    # Test email
    email_ok = test_email()
    
    # Test WhatsApp
    whatsapp_ok = test_whatsapp()
    
    # Summary
    print("\n" + "="*50)
    print("TEST SUMMARY")
    print("="*50)
    print(f"\n📧 Email: {'✅ WORKING' if email_ok else '❌ NOT WORKING'}")
    print(f"💬 WhatsApp: {'✅ WORKING' if whatsapp_ok else '❌ NOT WORKING'}")
    
    if email_ok and whatsapp_ok:
        print("\n🎉 All systems working! You're ready to go!")
    else:
        print("\n⚠️  Some systems need configuration")
        print("   See SETUP_CREDENTIALS.md for help")
    
    print("\n" + "="*50)

if __name__ == '__main__':
    main()
