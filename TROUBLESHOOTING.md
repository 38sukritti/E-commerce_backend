# 🚨 Quick Troubleshooting Guide

## Problem: Email Not Working

### Checklist:
- [ ] Installed python-dotenv: `pip install python-dotenv`
- [ ] Updated .env file with real Gmail address
- [ ] Generated Gmail App Password (16 characters)
- [ ] Enabled 2FA on Gmail account
- [ ] Restarted Django server after updating .env
- [ ] No spaces around = in .env file

### Quick Test:
```bash
cd finance-backend
python manage.py shell
```
```python
from django.core.mail import send_mail
from django.conf import settings
print(f"Email User: {settings.EMAIL_HOST_USER}")
print(f"Password Set: {bool(settings.EMAIL_HOST_PASSWORD)}")
send_mail('Test', 'Test message', settings.EMAIL_HOST_USER, [settings.CLIENT_EMAIL])
```

---

## Problem: WhatsApp Not Working

### Checklist:
- [ ] Created Twilio account
- [ ] Copied Account SID (starts with AC)
- [ ] Copied Auth Token
- [ ] Joined WhatsApp sandbox (sent join code)
- [ ] Phone numbers include country code (+919876543210)
- [ ] Updated .env file with Twilio credentials
- [ ] Restarted Django server

### Quick Test:
```bash
cd finance-backend
python manage.py shell
```
```python
from twilio.rest import Client
from django.conf import settings
client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
print(f"Account SID: {settings.TWILIO_ACCOUNT_SID[:10]}...")
# Replace with your number:
client.messages.create(
    from_=f'whatsapp:{settings.TWILIO_WHATSAPP_NUMBER}',
    body='Test',
    to='whatsapp:+919876543210'
)
```

---

## Problem: Environment Variables Not Loading

### Solution:
1. Check .env file location: `finance-backend/.env`
2. Verify no spaces: `KEY=value` not `KEY = value`
3. Restart server: `Ctrl+C` then `python manage.py runserver`
4. Check settings.py has:
   ```python
   from dotenv import load_dotenv
   load_dotenv(os.path.join(BASE_DIR, '.env'))
   ```

---

## Quick Commands

### Install Dependencies:
```bash
cd finance-backend
pip install -r requirements.txt
```

### Test Everything:
```bash
cd finance-backend
python test_credentials.py
```

### Run Server:
```bash
cd finance-backend
python manage.py runserver
```

---

## Getting Credentials

### Gmail App Password:
1. https://myaccount.google.com/security → Enable 2FA
2. https://myaccount.google.com/apppasswords → Generate
3. Copy 16-character password (no spaces)

### Twilio Credentials:
1. https://www.twilio.com/try-twilio → Sign up
2. https://console.twilio.com/ → Copy SID & Token
3. https://console.twilio.com/us1/develop/sms/try-it-out/whatsapp-learn → Join sandbox

---

## Still Not Working?

1. Check Django logs for error messages
2. Verify .env file has no typos
3. Make sure you saved .env file after editing
4. Try running: `python test_credentials.py`
5. Check spam folder for test emails
6. Verify Twilio account is active (not suspended)

## Need Help?

- Email setup: See EMAIL_TWILIO_SETUP.md
- Full guide: See SETUP_CREDENTIALS.md
- Test script: Run `python test_credentials.py`
