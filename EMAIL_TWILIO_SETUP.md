# Email & Twilio Setup Guide

## 🔧 Quick Fix Steps

### 1. Install Required Package
```bash
cd finance-backend
pip install python-dotenv
```

### 2. Configure Gmail for Email Sending

#### Step A: Enable 2-Factor Authentication
1. Go to https://myaccount.google.com/security
2. Enable "2-Step Verification"

#### Step B: Generate App Password
1. Go to https://myaccount.google.com/apppasswords
2. Select "Mail" and "Windows Computer"
3. Click "Generate"
4. Copy the 16-character password (remove spaces)

### 3. Configure Twilio for WhatsApp

#### Step A: Create Twilio Account
1. Sign up at https://www.twilio.com/try-twilio
2. Verify your phone number

#### Step B: Get Credentials
1. Go to https://console.twilio.com/
2. Copy your "Account SID" and "Auth Token"

#### Step C: Setup WhatsApp Sandbox
1. Go to https://console.twilio.com/us1/develop/sms/try-it-out/whatsapp-learn
2. Send the join code from your WhatsApp to the Twilio number
3. Copy the "From" WhatsApp number (format: +14155238886)

### 4. Update .env File

Edit `finance-backend/.env` with your real credentials:

```env
# Django Settings
SECRET_KEY=your-secret-key-here
DEBUG=True

# Email Configuration (Gmail SMTP)
EMAIL_HOST_USER=your-actual-email@gmail.com
EMAIL_HOST_PASSWORD=your-16-char-app-password
CLIENT_EMAIL=email-where-you-want-to-receive-inquiries@gmail.com

# Twilio Configuration
TWILIO_ACCOUNT_SID=ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
TWILIO_AUTH_TOKEN=your-auth-token-here
TWILIO_WHATSAPP_NUMBER=+14155238886
```

### 5. Test Your Configuration

Run the test script:
```bash
python test_credentials.py
```

## 🚨 Common Issues & Solutions

### Email Not Sending
- ✅ Make sure you're using an App Password, not your regular Gmail password
- ✅ Check that 2FA is enabled on your Google account
- ✅ Verify EMAIL_HOST_USER and CLIENT_EMAIL are valid email addresses
- ✅ Check for typos in your .env file

### WhatsApp Not Sending
- ✅ Make sure you've joined the Twilio WhatsApp sandbox
- ✅ Phone numbers must include country code (e.g., +919876543210)
- ✅ Verify your Twilio account is active (not suspended)
- ✅ Check that TWILIO_ACCOUNT_SID starts with "AC"

### Environment Variables Not Loading
- ✅ Make sure .env file is in the finance-backend folder
- ✅ Restart your Django server after updating .env
- ✅ Check for spaces around the = sign in .env (should be KEY=value)

## 📝 Testing Individual Components

### Test Email Only
```python
from django.core.mail import send_mail
from django.conf import settings

send_mail(
    'Test Email',
    'This is a test message.',
    settings.EMAIL_HOST_USER,
    [settings.CLIENT_EMAIL],
    fail_silently=False,
)
```

### Test Twilio Only
```python
from twilio.rest import Client
from django.conf import settings

client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
message = client.messages.create(
    from_=f'whatsapp:{settings.TWILIO_WHATSAPP_NUMBER}',
    body='Test message from Grovix Studio',
    to='whatsapp:+919876543210'  # Replace with your number
)
print(f"Message sent: {message.sid}")
```

## 🎯 Next Steps

1. Install python-dotenv: `pip install python-dotenv`
2. Update your .env file with real credentials
3. Restart Django server
4. Test the contact form

## 💡 Pro Tips

- Keep your .env file secure and never commit it to Git
- Use different email addresses for EMAIL_HOST_USER and CLIENT_EMAIL
- For production, consider using Twilio's verified numbers instead of sandbox
- Monitor your Twilio usage to avoid unexpected charges
