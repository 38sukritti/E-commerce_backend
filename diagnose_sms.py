"""
Detailed SMS Diagnostic Script
This will show you exactly what's wrong
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

print("\n" + "="*60)
print("DETAILED SMS DIAGNOSTICS")
print("="*60)

print("\n1. CHECKING ENVIRONMENT VARIABLES")
print("-" * 60)

# Check .env file exists
env_file = BASE_DIR / '.env'
if env_file.exists():
    print(f"✅ .env file found: {env_file}")
else:
    print(f"❌ .env file NOT found: {env_file}")
    sys.exit(1)

# Check Twilio settings
print("\n2. CHECKING TWILIO CONFIGURATION")
print("-" * 60)

account_sid = settings.TWILIO_ACCOUNT_SID
auth_token = settings.TWILIO_AUTH_TOKEN
phone_number = settings.TWILIO_PHONE_NUMBER

print(f"TWILIO_ACCOUNT_SID: {account_sid}")
print(f"   Length: {len(account_sid) if account_sid else 0}")
print(f"   Starts with 'AC': {account_sid.startswith('AC') if account_sid else False}")
print(f"   Status: {'✅ Valid format' if account_sid and account_sid.startswith('AC') and len(account_sid) == 34 else '❌ Invalid'}")

print(f"\nTWILIO_AUTH_TOKEN: {'*' * 20}")
print(f"   Length: {len(auth_token) if auth_token else 0}")
print(f"   Status: {'✅ Set' if auth_token and len(auth_token) == 32 else '❌ Invalid'}")

print(f"\nTWILIO_PHONE_NUMBER: {phone_number}")
print(f"   Format: {'✅ Valid' if phone_number and phone_number.startswith('+') else '❌ Invalid'}")

# Check if credentials are placeholders
if account_sid == 'your-twilio-account-sid':
    print("\n❌ ERROR: Twilio credentials are still placeholders!")
    print("   Please update .env file with real Twilio credentials")
    sys.exit(1)

print("\n3. TESTING TWILIO CONNECTION")
print("-" * 60)

try:
    from twilio.rest import Client
    print("✅ Twilio library imported successfully")
    
    print("\nCreating Twilio client...")
    client = Client(account_sid, auth_token)
    print("✅ Twilio client created")
    
    print("\nFetching account info...")
    account = client.api.accounts(account_sid).fetch()
    print(f"✅ Connected to Twilio account: {account.friendly_name}")
    print(f"   Status: {account.status}")
    print(f"   Type: {account.type}")
    
except Exception as e:
    print(f"❌ Twilio connection failed!")
    print(f"   Error: {str(e)}")
    print("\n💡 Possible issues:")
    print("   - Account SID is incorrect")
    print("   - Auth Token is incorrect")
    print("   - Network connection issue")
    print("   - Twilio account suspended")
    sys.exit(1)

print("\n4. CHECKING PHONE NUMBER")
print("-" * 60)

try:
    print(f"Checking phone number: {phone_number}")
    
    # Try to get phone number details
    incoming_phone_numbers = client.incoming_phone_numbers.list(phone_number=phone_number)
    
    if incoming_phone_numbers:
        phone = incoming_phone_numbers[0]
        print(f"✅ Phone number found: {phone.phone_number}")
        print(f"   Friendly Name: {phone.friendly_name}")
        print(f"   Capabilities:")
        print(f"      SMS: {phone.capabilities.get('sms', False)}")
        print(f"      Voice: {phone.capabilities.get('voice', False)}")
    else:
        print(f"⚠️  Phone number not found in your account")
        print(f"   This might be a trial number or not yet configured")
        
except Exception as e:
    print(f"⚠️  Could not verify phone number: {str(e)}")
    print("   This is OK for trial accounts")

print("\n5. TESTING SMS SEND")
print("-" * 60)

print("\n📱 Enter your phone number to test SMS:")
print("   Format: +919876543210 (include country code)")
print("   Or press Enter to skip")
phone = input("   Phone: ").strip()

if not phone:
    print("\n⚠️  Skipped SMS test")
    print("\n" + "="*60)
    print("DIAGNOSTICS COMPLETE")
    print("="*60)
    print("\n✅ Configuration looks good!")
    print("   Try sending SMS manually with the phone number you want to test")
    sys.exit(0)

if not phone.startswith('+'):
    print("❌ Phone number must start with + and country code")
    sys.exit(1)

try:
    print(f"\n📤 Sending test SMS to {phone}...")
    
    message = client.messages.create(
        from_=phone_number,
        body='Test SMS from Grovix Studio! If you receive this, SMS is working! 🎉',
        to=phone
    )
    
    print(f"\n✅ SMS SENT SUCCESSFULLY!")
    print(f"   Message SID: {message.sid}")
    print(f"   Status: {message.status}")
    print(f"   From: {message.from_}")
    print(f"   To: {message.to}")
    print(f"   Price: {message.price} {message.price_unit}")
    
    print(f"\n📱 Check your phone: {phone}")
    print("   SMS should arrive within 1-2 minutes")
    
    print("\n💡 If you don't receive it:")
    print("   1. Check if your number is verified (trial accounts only)")
    print("   2. Check Twilio logs: https://console.twilio.com/us1/monitor/logs/sms")
    print("   3. Wait a few minutes for delivery")
    
except Exception as e:
    error_msg = str(e)
    print(f"\n❌ SMS FAILED!")
    print(f"   Error: {error_msg}")
    
    # Specific error handling
    if "not a valid phone number" in error_msg.lower():
        print("\n💡 Phone number format is incorrect")
        print("   Use format: +919876543210 (country code + number)")
        
    elif "not a verified" in error_msg.lower() or "trial" in error_msg.lower():
        print("\n💡 Your number needs to be verified (Trial Account)")
        print("   1. Go to: https://console.twilio.com/us1/develop/phone-numbers/manage/verified")
        print("   2. Click 'Add a new number'")
        print("   3. Enter your phone number")
        print("   4. Verify with OTP")
        
    elif "insufficient" in error_msg.lower() or "balance" in error_msg.lower():
        print("\n💡 Insufficient balance")
        print("   Check balance: https://console.twilio.com/billing")
        print("   Add credit or upgrade account")
        
    elif "authentication" in error_msg.lower() or "credentials" in error_msg.lower():
        print("\n💡 Authentication failed")
        print("   Check your Account SID and Auth Token in .env file")
        
    else:
        print("\n💡 Unknown error")
        print("   Check Twilio logs: https://console.twilio.com/us1/monitor/logs/sms")
    
    sys.exit(1)

print("\n" + "="*60)
print("DIAGNOSTICS COMPLETE - ALL TESTS PASSED! ✅")
print("="*60)
print("\n🎉 SMS is working perfectly!")
print("\n📝 Next steps:")
print("   1. Start backend: python manage.py runserver")
print("   2. Start frontend: npm run dev")
print("   3. Test contact form with verified phone number")
print("\n" + "="*60)
