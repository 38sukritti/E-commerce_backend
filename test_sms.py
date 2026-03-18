"""
Quick SMS Test Script
Run this to test if SMS is working
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
from twilio.rest import Client

def test_sms():
    print("\n" + "="*50)
    print("TESTING SMS CONFIGURATION")
    print("="*50)
    
    print(f"\n📱 Twilio Settings:")
    print(f"   Account SID: {settings.TWILIO_ACCOUNT_SID[:10]}...")
    print(f"   Phone Number: {settings.TWILIO_PHONE_NUMBER}")
    
    if settings.TWILIO_ACCOUNT_SID == 'your-twilio-account-sid':
        print("\n❌ Twilio NOT configured!")
        print("   Please edit .env file with your Twilio credentials")
        return False
    
    # Ask for phone number
    print("\n📱 Enter your phone number to test SMS:")
    print("   Format: +919876543210 (include country code)")
    phone = input("   Phone: ").strip()
    
    if not phone.startswith('+'):
        print("❌ Phone number must start with + and country code")
        return False
    
    try:
        print(f"\n📤 Sending test SMS to {phone}...")
        client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
        
        message = client.messages.create(
            from_=settings.TWILIO_PHONE_NUMBER,
            body='🎉 Test SMS from Grovix Studio! If you receive this, SMS is working!',
            to=phone
        )
        
        print(f"✅ SMS sent successfully!")
        print(f"   Message SID: {message.sid}")
        print(f"   Status: {message.status}")
        print(f"   Check your phone: {phone}")
        print("\n💡 If you don't receive it:")
        print("   1. Verify your number in Twilio console")
        print("   2. Check Twilio logs: https://console.twilio.com/us1/monitor/logs/sms")
        print("   3. Wait 1-2 minutes for delivery")
        return True
    except Exception as e:
        print(f"❌ SMS failed: {str(e)}")
        print("\n💡 Common issues:")
        print("   - Phone number not verified (trial account)")
        print("   - Phone number format incorrect")
        print("   - Twilio credentials incorrect")
        print("   - Insufficient balance")
        print("\n🔗 Verify your number here:")
        print("   https://console.twilio.com/us1/develop/phone-numbers/manage/verified")
        return False

def main():
    print("\n" + "="*50)
    print("GROVIX STUDIO - SMS TEST")
    print("="*50)
    print("\nThis script will test your SMS configuration")
    print("Make sure you've edited the .env file first!")
    
    input("\nPress Enter to start testing...")
    
    sms_ok = test_sms()
    
    print("\n" + "="*50)
    print("TEST SUMMARY")
    print("="*50)
    print(f"\n📱 SMS: {'✅ WORKING' if sms_ok else '❌ NOT WORKING'}")
    
    if sms_ok:
        print("\n🎉 SMS is working! You're ready to go!")
        print("\n📝 Next steps:")
        print("   1. Start backend: python manage.py runserver")
        print("   2. Start frontend: npm run dev")
        print("   3. Test contact form")
    else:
        print("\n⚠️  SMS needs configuration")
        print("   See SMS_SETUP_GUIDE.md for help")
    
    print("\n" + "="*50)

if __name__ == '__main__':
    main()
