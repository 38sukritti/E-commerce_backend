# 📧 Email & WhatsApp Flow

## How It Works Now

```
┌─────────────────────────────────────────────────────────────┐
│                    CUSTOMER FILLS FORM                       │
│  Name: John Doe                                              │
│  Email: john@example.com                                     │
│  Phone: +919876543210                                        │
│  Plan: Premium Package                                       │
└─────────────────────────────────────────────────────────────┘
                            │
                            ▼
        ┌───────────────────────────────────────┐
        │      FORM SUBMITTED TO BACKEND        │
        └───────────────────────────────────────┘
                            │
                ┌───────────┴───────────┐
                │                       │
                ▼                       ▼
    ┌─────────────────────┐   ┌─────────────────────┐
    │   EMAIL SENT TO:    │   │  WHATSAPP SENT TO:  │
    │   YOUR BUSINESS     │   │   CUSTOMER'S PHONE  │
    │                     │   │                     │
    │ CLIENT_EMAIL        │   │ +919876543210       │
    │ (You receive it)    │   │ (Customer receives) │
    │                     │   │                     │
    │ Contains:           │   │ From:               │
    │ - Customer details  │   │ Your Twilio number  │
    │ - Inquiry ID        │   │ +14155238886        │
    │ - Selected plan     │   │                     │
    │ - Message           │   │ Contains:           │
    │                     │   │ - Thank you message │
    │ Reply-To:           │   │ - Inquiry ID        │
    │ john@example.com    │   │ - Next steps        │
    └─────────────────────┘   └─────────────────────┘
```

## Configuration in .env

```env
# ============================================
# EMAIL CONFIGURATION
# ============================================

# Your Gmail account (SENDS the emails)
EMAIL_HOST_USER=your-business@gmail.com
EMAIL_HOST_PASSWORD=abcd efgh ijkl mnop  # 16-char app password

# Where YOU receive inquiry notifications
CLIENT_EMAIL=your-business@gmail.com
# (Can be same as EMAIL_HOST_USER or different)

# ============================================
# WHATSAPP CONFIGURATION
# ============================================

# Your Twilio credentials
TWILIO_ACCOUNT_SID=ACxxxxxxxxxxxxxxxxxxxxx
TWILIO_AUTH_TOKEN=your-auth-token-here

# Your registered Twilio WhatsApp number (SENDS messages)
TWILIO_WHATSAPP_NUMBER=+14155238886
```

## Example Scenario

### Customer submits form:
- **Name**: Rajesh Kumar
- **Email**: rajesh@company.com
- **Phone**: +919876543210
- **Plan**: Premium Package

### What happens:

1. **Email to YOU** (CLIENT_EMAIL):
   ```
   To: your-business@gmail.com
   From: your-business@gmail.com
   Reply-To: rajesh@company.com
   Subject: New Inquiry - INQ001 - Premium Package
   
   [Beautiful HTML email with all customer details]
   
   When you click Reply, it will reply to: rajesh@company.com
   ```

2. **WhatsApp to CUSTOMER** (+919876543210):
   ```
   From: +14155238886 (Your Twilio number)
   To: +919876543210 (Customer's phone)
   
   🎉 Thank You for Choosing Grovix Studio!
   
   Dear Rajesh Kumar,
   
   Inquiry ID: INQ001
   Selected Plan: Premium Package
   
   We'll contact you within 24 hours...
   ```

## Key Points

✅ **Only ONE email sent** → To your business (CLIENT_EMAIL)
✅ **WhatsApp sent to customer** → Using their phone number from form
✅ **You can reply to customer email** → Reply-To header is set
✅ **Customer gets confirmation** → Via WhatsApp to their number

## Testing

After updating your .env file, test with:

```bash
cd finance-backend
python test_credentials.py
```

This will:
1. Send test email to YOUR business email (CLIENT_EMAIL)
2. Ask for YOUR phone number to test WhatsApp
3. Verify both are working correctly

## Need to Change?

### Use different email for sending vs receiving:
```env
EMAIL_HOST_USER=noreply@yourdomain.com  # Sends emails
CLIENT_EMAIL=inquiries@yourdomain.com   # Receives inquiries
```

### Use Twilio verified number (production):
```env
TWILIO_WHATSAPP_NUMBER=+919876543210  # Your registered business number
```
(Requires Twilio account upgrade from sandbox)
