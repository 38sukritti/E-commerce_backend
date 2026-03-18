# 📧 EMAIL & WHATSAPP SETUP GUIDE

## Current Status
❌ Email not configured (placeholder credentials)
❌ WhatsApp not configured (placeholder credentials)

## What Works Without Configuration
✅ Form submission
✅ Database storage
✅ Excel file creation
✅ Admin panel

## What Needs Configuration
❌ Email to client
❌ WhatsApp to customer

---

## 📧 GMAIL SMTP SETUP (For Email)

### Step 1: Enable 2-Factor Authentication
1. Go to: https://myaccount.google.com/security
2. Click "2-Step Verification"
3. Follow the setup wizard

### Step 2: Generate App Password
1. Go to: https://myaccount.google.com/apppasswords
2. Select "Mail" and "Windows Computer"
3. Click "Generate"
4. Copy the 16-character password (e.g., abcd efgh ijkl mnop)

### Step 3: Edit .env File
Open: `finance-backend\.env`

Replace these lines:
```env
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-gmail-app-password
CLIENT_EMAIL=client-email@example.com
```

With your actual values:
```env
EMAIL_HOST_USER=youremail@gmail.com
EMAIL_HOST_PASSWORD=abcd efgh ijkl mnop
CLIENT_EMAIL=client@example.com
```

**Example:**
```env
EMAIL_HOST_USER=grovixstudio@gmail.com
EMAIL_HOST_PASSWORD=xyzw abcd efgh ijkl
CLIENT_EMAIL=shivesh@grovixstudio.com
```

---

## 💬 TWILIO WHATSAPP SETUP (For WhatsApp)

### Step 1: Create Twilio Account
1. Go to: https://www.twilio.com/try-twilio
2. Sign up (free trial with $15 credit)
3. Verify your phone number

### Step 2: Get Credentials
1. Go to Console Dashboard: https://console.twilio.com/
2. Copy **Account SID** (starts with AC...)
3. Copy **Auth Token**

### Step 3: Activate WhatsApp Sandbox
1. Go to: Messaging → Try it out → Send a WhatsApp message
2. You'll see a code like: "join abc-xyz"
3. Open WhatsApp on your phone
4. Send message to: **+1 415 523 8886**
5. Type: **join abc-xyz** (use your actual code)
6. You'll receive confirmation

### Step 4: Edit .env File
Open: `finance-backend\.env`

Replace these lines:
```env
TWILIO_ACCOUNT_SID=your-twilio-account-sid
TWILIO_AUTH_TOKEN=your-twilio-auth-token
```

With your actual values:
```env
TWILIO_ACCOUNT_SID=ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
TWILIO_AUTH_TOKEN=your-actual-auth-token-here
```

**Note:** Keep `TWILIO_WHATSAPP_NUMBER=+14155238886` as is (Twilio sandbox number)

---

## 🔄 After Configuration

### 1. Restart Django Server
Stop the server (Ctrl+C) and restart:
```bash
cd finance-backend
python manage.py runserver
```

### 2. Test the System
1. Go to: http://localhost:5173
2. Click "Pricing"
3. Select a plan
4. Fill the form with YOUR phone number (format: +919876543210)
5. Submit

### 3. Check Results
✅ Email sent to CLIENT_EMAIL
✅ WhatsApp sent to your phone
✅ Excel file updated
✅ Entry in admin panel

---

## 🐛 Troubleshooting

### Email Not Sending

**Check:**
- ✅ 2FA enabled on Gmail
- ✅ App password is 16 characters
- ✅ No spaces in password (or keep spaces as shown)
- ✅ EMAIL_HOST_USER is correct
- ✅ CLIENT_EMAIL is correct
- ✅ Check spam folder

**Test Email Manually:**
```python
# In Django shell
python manage.py shell

from django.core.mail import send_mail
send_mail(
    'Test Subject',
    'Test Message',
    'your-email@gmail.com',
    ['client-email@example.com'],
    fail_silently=False,
)
```

### WhatsApp Not Sending

**Check:**
- ✅ Twilio account active
- ✅ WhatsApp sandbox joined
- ✅ Phone number format: +[country][number]
- ✅ No spaces in phone number
- ✅ Twilio credentials correct
- ✅ Twilio account has balance

**Test WhatsApp Manually:**
```python
# In Django shell
python manage.py shell

from twilio.rest import Client
client = Client('your-sid', 'your-token')
message = client.messages.create(
    from_='whatsapp:+14155238886',
    body='Test message',
    to='whatsapp:+919876543210'
)
print(message.sid)
```

---

## 📝 Quick Reference

### .env File Template
```env
# Django Settings
SECRET_KEY=your-secret-key-here
DEBUG=True

# Email Configuration (Gmail SMTP)
EMAIL_HOST_USER=youremail@gmail.com
EMAIL_HOST_PASSWORD=abcd efgh ijkl mnop
CLIENT_EMAIL=client@example.com

# Twilio Configuration
TWILIO_ACCOUNT_SID=ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
TWILIO_AUTH_TOKEN=your-auth-token-here
TWILIO_WHATSAPP_NUMBER=+14155238886
```

### Phone Number Format
✅ Correct: +919876543210
❌ Wrong: 9876543210 (missing +91)
❌ Wrong: +91 98765 43210 (has spaces)

### Email Format
✅ Correct: user@gmail.com
❌ Wrong: user@gmail (missing .com)

---

## 🎯 Testing Checklist

Before going live:
- [ ] Gmail credentials configured
- [ ] Twilio credentials configured
- [ ] WhatsApp sandbox joined
- [ ] Test email received
- [ ] Test WhatsApp received
- [ ] Excel file created
- [ ] Admin panel accessible
- [ ] Form validation works
- [ ] Success page shows

---

## 💡 Tips

1. **Use a dedicated email** for sending (not your personal email)
2. **Test with your own phone** first before using customer numbers
3. **Check Twilio balance** regularly
4. **Backup Excel file** periodically
5. **Monitor admin panel** for new inquiries

---

## 📞 Need Help?

If you're stuck:
1. Check Django server console for errors
2. Check browser console for errors
3. Verify all credentials are correct
4. Try testing email/WhatsApp separately
5. Check spam folder for emails

---

**Once configured, everything will work automatically! 🚀**
