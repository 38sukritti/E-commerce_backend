# Grovix Studio Backend - Django

Complete backend system for handling customer inquiries with email notifications, WhatsApp messages, and Excel tracking.

## Features

✅ **Customer Inquiry Management**
- Store all customer inquiries in database
- Auto-generate unique inquiry IDs (GRV######)
- Track all customer details and selected plans

✅ **Email Notifications (SMTP)**
- Beautiful HTML email sent to client
- Includes all inquiry details
- Professional styling matching brand

✅ **WhatsApp Notifications (Twilio)**
- Automatic confirmation message to customers
- Professional thank you message
- Includes inquiry ID and next steps

✅ **Excel Tracking (OpenPyXL)**
- Auto-update Excel sheet with new inquiries
- Formatted headers and auto-adjusted columns
- Easy to share and analyze

✅ **Admin Dashboard**
- Django admin interface for managing inquiries
- Search, filter, and export capabilities
- View all customer details

## Installation

### 1. Install Dependencies

```bash
cd finance-backend
pip install -r requirements.txt
```

### 2. Configure Environment Variables

Create a `.env` file (copy from `.env.example`):

```bash
cp .env.example .env
```

Edit `.env` with your credentials:

```env
# Email Configuration (Gmail)
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-gmail-app-password
CLIENT_EMAIL=client-email@example.com

# Twilio Configuration
TWILIO_ACCOUNT_SID=your-twilio-account-sid
TWILIO_AUTH_TOKEN=your-twilio-auth-token
TWILIO_WHATSAPP_NUMBER=+14155238886
```

### 3. Setup Gmail SMTP

1. Go to Google Account Settings
2. Enable 2-Factor Authentication
3. Generate App Password:
   - Go to Security → App Passwords
   - Select "Mail" and "Windows Computer"
   - Copy the 16-character password
   - Use this in `EMAIL_HOST_PASSWORD`

### 4. Setup Twilio WhatsApp

1. Sign up at [Twilio](https://www.twilio.com/)
2. Get your Account SID and Auth Token
3. Activate WhatsApp Sandbox:
   - Go to Messaging → Try it out → Send a WhatsApp message
   - Follow instructions to connect your WhatsApp
4. Use sandbox number: `+14155238886`

### 5. Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Create Superuser

```bash
python manage.py createsuperuser
```

### 7. Run Development Server

```bash
python manage.py runserver
```

Server will run at: `http://127.0.0.1:8000`

## API Endpoints

### Contact Form Submission
```
POST /api/submit-inquiry/
Content-Type: application/json

{
  "name": "John Doe",
  "email": "john@example.com",
  "phone": "+919876543210",
  "company": "ABC Corp",
  "selected_plan": "Growth",
  "message": "I need a website"
}
```

### Contact Page (with pre-selected plan)
```
GET /contact/?plan=Growth
```

## Frontend Integration

Update your pricing buttons to redirect to contact page with plan parameter:

```javascript
// Example for pricing.js
button.addEventListener('click', () => {
  const plan = button.getAttribute('data-plan');
  window.location.href = `http://127.0.0.1:8000/contact/?plan=${encodeURIComponent(plan)}`;
});
```

## Admin Dashboard

Access admin at: `http://127.0.0.1:8000/admin/`

Features:
- View all inquiries
- Search by name, email, phone
- Filter by plan and date
- Export to CSV

## Excel File

The `inquiries_data.xlsx` file is automatically created in the project root directory.

Columns:
- Inquiry ID
- Date
- Name
- Email
- Phone
- Company
- Selected Plan
- Message

## Deployment

### Option 1: Railway

1. Install Railway CLI:
```bash
npm install -g @railway/cli
```

2. Login and deploy:
```bash
railway login
railway init
railway up
```

3. Add environment variables in Railway dashboard

### Option 2: Heroku

1. Install Heroku CLI
2. Create `Procfile`:
```
web: gunicorn grovix_backend.wsgi
```

3. Deploy:
```bash
heroku create grovix-backend
git push heroku main
heroku run python manage.py migrate
```

### Option 3: PythonAnywhere

1. Upload code to PythonAnywhere
2. Create virtual environment
3. Configure WSGI file
4. Set environment variables

## Environment Variables for Production

```env
DEBUG=False
ALLOWED_HOSTS=your-domain.com,www.your-domain.com
SECRET_KEY=generate-new-secret-key

EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
CLIENT_EMAIL=client@example.com

TWILIO_ACCOUNT_SID=your-sid
TWILIO_AUTH_TOKEN=your-token
TWILIO_WHATSAPP_NUMBER=+14155238886
```

## Security Notes

⚠️ **Important:**
- Never commit `.env` file to Git
- Use strong SECRET_KEY in production
- Set `DEBUG=False` in production
- Configure `ALLOWED_HOSTS` properly
- Use HTTPS in production
- Regularly update dependencies

## Troubleshooting

### Email not sending
- Check Gmail app password is correct
- Ensure 2FA is enabled on Gmail
- Check "Less secure app access" is OFF (use app password instead)

### WhatsApp not sending
- Verify Twilio credentials
- Check WhatsApp sandbox is activated
- Ensure phone number format: +[country code][number]
- Check Twilio account balance

### Excel file not updating
- Check file permissions
- Ensure openpyxl is installed
- Verify BASE_DIR path is correct

## Support

For issues or questions:
- Email: hello@grovixstudio.com
- Phone: +91 70090 66489

---

**Built with ❤️ for Grovix Studio**
