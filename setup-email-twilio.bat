@echo off
echo ========================================
echo Grovix Studio - Email & Twilio Setup
echo ========================================
echo.

cd finance-backend

echo [1/3] Installing python-dotenv...
pip install python-dotenv
echo.

echo [2/3] Checking .env file...
if not exist .env (
    echo ERROR: .env file not found!
    echo Please create .env file from .env.example
    pause
    exit /b 1
)
echo .env file found!
echo.

echo [3/3] Testing credentials...
echo.
python test_credentials.py

echo.
echo ========================================
echo Setup Complete!
echo ========================================
pause
