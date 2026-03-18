@echo off
echo ========================================
echo Grovix Studio Backend Setup
echo ========================================
echo.

echo [1/6] Installing dependencies...
pip install -r requirements.txt

echo.
echo [2/6] Creating .env file...
if not exist .env (
    copy .env.example .env
    echo .env file created! Please edit it with your credentials.
) else (
    echo .env file already exists.
)

echo.
echo [3/6] Running migrations...
python manage.py makemigrations
python manage.py migrate

echo.
echo [4/6] Creating superuser...
echo Please create an admin account:
python manage.py createsuperuser

echo.
echo [5/6] Collecting static files...
python manage.py collectstatic --noinput

echo.
echo ========================================
echo Setup Complete!
echo ========================================
echo.
echo Next steps:
echo 1. Edit .env file with your credentials
echo 2. Run: python manage.py runserver
echo 3. Access admin: http://127.0.0.1:8000/admin/
echo 4. Access contact: http://127.0.0.1:8000/contact/
echo.
echo ========================================
pause
