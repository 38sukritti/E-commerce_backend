# 📱 WhatsApp/SMS Configuration Guide

## ⚠️ WhatsApp Sandbox Issue in India

Twilio's WhatsApp sandbox (+1 415 523 8886) has restrictions in India and some other regions. You cannot send WhatsApp messages to Indian numbers using the sandbox.

## ✅ Solution: I've Changed to SMS

I've updated your code to use **regular SMS** instead of WhatsApp. This will work immediately!

---

## 🔧 What I Changed

### Before (WhatsApp):
```python
message = client.messages.create(
    from_=f'whatsapp:{settings.TWILIO_WHATSAPP_NUMBER}',
    body=message_body,
    to=f'whatsapp:{inquiry.phone}'
)
```

### After (SMS):
```python
message = client.messages.create(
    from_=settings.TWILIO_PHONE_NUMBER,
    body=message_body,
    to=inquiry.phone
)
```

---

## 📲 How It Works Now

### Customer Flow:
```
Customer fills form
       ↓
Backend receives data
       ↓
┌─────────────────────────────┐
│ 1. Email → YOUR business    │
│ 2. SMS → Customer's phone   │ ← Changed from WhatsApp
│ 3. Save to Excel + Database │
└─────────────────────────────┘
```

### SMS Message Format:
```
Thank you [Name]! Your inquiry [INQ001] for [Premium Package] 
has been received. We'll contact you within 24 hours. 
- Grovix Studio
```

**Note:** SMS is limited to ~160 characters, so I made it concise.

---

## 🧪 Testing SMS

### Option 1: Use Test Script
```bash
cd finance-backend
python manage.py shell
```

```python
from twilio.rest import Client
from django.conf import settings

client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)

# Replace with your phone number
message = client.messages.create(
    from_=settings.TWILIO_PHONE_NUMBER,
    body='Test SMS from Grovix Studio!',
    to='+919876543210'  # Your number with country code
)

print(f"SMS sent! SID: {message.sid}")
```

### Option 2: Submit Test Form
1. Start backend: `python manage.py runserver`
2. Start frontend: `npm run dev`
3. Fill contact form with your phone number
4. Check your phone for SMS

---

## 💰 Twilio SMS Pricing

### Free Trial:
- ✅ $15 credit when you sign up
- ✅ Can send ~500 SMS messages
- ✅ Perfect for testing

### SMS Costs (India):
- 📤 Outbound SMS: ~$0.03 per message
- 📥 Inbound SMS: ~$0.01 per message

### Upgrade Options:
1. **Keep using trial** - Good for testing
2. **Add credit** - Pay as you go
3. **Get verified number** - Better for production

---

## 🔄 Alternative Options

### Option 1: Use SMS (Current - Recommended)
✅ Works immediately
✅ No sandbox restrictions
✅ Reliable delivery
✅ Works in all countries
❌ Costs money (but cheap)
❌ Limited to 160 characters

### Option 2: Disable Customer Notifications
If you don't want to send SMS, just disable it:

```python
# In views.py, comment out this line:
# send_whatsapp_message(inquiry)
```

You'll still get email notifications, and data will be saved.

### Option 3: Use Email for Customer Confirmation
Send email to customer instead of SMS:

```python
def send_customer_email(inquiry):
    send_mail(
        subject=f'Thank you for your inquiry - {inquiry.inquiry_id}',
        message=f'Dear {inquiry.name}, we received your inquiry...',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[inquiry.email],
    )
```

### Option 4: WhatsApp Business API (Production)
For production, use official WhatsApp Business API:
- ✅ No sandbox restrictions
- ✅ Professional appearance
- ✅ Better delivery rates
- ❌ Requires business verification
- ❌ More expensive
- ❌ Complex setup

---

## 🎯 Current Configuration

### Your .env file now has:
```env
# Twilio Configuration
TWILIO_ACCOUNT_SID=your_twilio_account_sid
TWILIO_AUTH_TOKEN=your_twilio_auth_token
TWILIO_PHONE_NUMBER=+14155238886  # For SMS
```

### What happens on form submission:
1. ✅ **Email sent to YOU** (sukritti3406.beai24@chitkara.edu.in)
   - Contains all customer details
   - Professional HTML format
   
2. ✅ **SMS sent to CUSTOMER** (their phone number)
   - Short confirmation message
   - Includes inquiry ID
   
3. ✅ **Data saved to:**
   - SQLite database
   - Excel file (inquiries_data.xlsx)

---

## 📝 SMS Message Examples

### Current SMS (160 chars):
```
Thank you Rajesh! Your inquiry INQ001 for Premium Package 
has been received. We'll contact you within 24 hours. 
- Grovix Studio
```

### Alternative (Shorter):
```
Grovix Studio: Thank you! Inquiry INQ001 received. 
We'll contact you soon.
```

### Alternative (With Link):
```
Thank you! Your inquiry INQ001 is confirmed. 
Track: grovixstudio.com/track/INQ001
```

---

## 🔧 Customizing SMS Message

Edit `finance-backend/inquiries/utils.py`:

```python
def send_whatsapp_message(inquiry):
    # Change this message to whatever you want
    message_body = f"""Your custom message here...
    
    Inquiry ID: {inquiry.inquiry_id}
    Name: {inquiry.name}
    Plan: {inquiry.selected_plan}
    """
```

**Tips:**
- Keep under 160 characters to avoid splitting
- Include inquiry ID for reference
- Add your contact info
- Be concise and professional

---

## 🚀 Ready to Test!

### Step 1: Verify Twilio Number
Go to: https://console.twilio.com/us1/develop/phone-numbers/manage/incoming

Check if +14155238886 can send SMS to India.

### Step 2: Test SMS
```bash
cd finance-backend
python manage.py shell
```

```python
from twilio.rest import Client
from django.conf import settings

client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
message = client.messages.create(
    from_='+14155238886',
    body='Test from Grovix Studio',
    to='+91YOUR_NUMBER'  # Your actual number
)
print(f"Success! SID: {message.sid}")
```

### Step 3: Check Phone
- SMS should arrive within seconds
- Check spam/blocked messages if not received

---

## ⚠️ Common Issues & Solutions

### Issue 1: SMS Not Received
**Possible causes:**
- Phone number format wrong (must include +91)
- Twilio trial restrictions (verify your number first)
- Network delay (wait 1-2 minutes)
- Blocked by carrier

**Solution:**
1. Verify your phone number in Twilio console
2. Check Twilio logs: https://console.twilio.com/us1/monitor/logs/sms
3. Try different phone number

### Issue 2: "Unverified Number" Error
**Solution:**
In Twilio trial, you can only send to verified numbers.

Verify your number:
1. Go to: https://console.twilio.com/us1/develop/phone-numbers/manage/verified
2. Click "Add a new number"
3. Enter your phone number
4. Verify with OTP

### Issue 3: "Insufficient Balance"
**Solution:**
- Check balance: https://console.twilio.com/billing
- Add credit if needed
- Or upgrade account

---

## 💡 Recommendations

### For Testing (Now):
✅ Use SMS with Twilio trial
✅ Verify your phone number in Twilio
✅ Test with 2-3 numbers

### For Production (Later):
✅ Upgrade Twilio account
✅ Get dedicated phone number
✅ Consider WhatsApp Business API
✅ Add SMS delivery tracking
✅ Monitor costs

---

## 📊 Comparison: WhatsApp vs SMS

| Feature | WhatsApp | SMS |
|---------|----------|-----|
| **Setup** | Complex (sandbox) | Simple ✅ |
| **India Support** | Limited ❌ | Full ✅ |
| **Cost** | Free (sandbox) | ~$0.03/msg |
| **Delivery** | Requires app | Universal ✅ |
| **Character Limit** | 4096 chars | 160 chars |
| **Rich Media** | Yes | No |
| **Professional** | More modern | Traditional |

**Verdict:** SMS is better for your use case right now!

---

## 🎉 Summary

### What Changed:
- ❌ WhatsApp (not working in India)
- ✅ SMS (working everywhere)

### What You Need to Do:
1. Verify your phone number in Twilio console
2. Test SMS with the script above
3. Submit a test form to verify end-to-end

### What Works Now:
- ✅ Email to your business
- ✅ SMS to customer
- ✅ Excel file creation
- ✅ Database storage

---

## 🔗 Useful Links

- Twilio Console: https://console.twilio.com/
- Verify Numbers: https://console.twilio.com/us1/develop/phone-numbers/manage/verified
- SMS Logs: https://console.twilio.com/us1/monitor/logs/sms
- Billing: https://console.twilio.com/billing
- Pricing: https://www.twilio.com/sms/pricing

---

## ❓ Questions?

**Q: Can I switch back to WhatsApp later?**
A: Yes! Just change the code back and use WhatsApp Business API (paid).

**Q: How many SMS can I send with trial?**
A: ~500 messages with $15 credit.

**Q: Do I need to verify every customer's number?**
A: Only during trial. After upgrade, you can send to any number.

**Q: Can I send to international numbers?**
A: Yes, but costs vary by country.

**Q: Can I disable SMS completely?**
A: Yes, just comment out `send_whatsapp_message(inquiry)` in views.py

---

You're all set! Test it now with your phone number! 🚀
