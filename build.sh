#!/usr/bin/env bash
# exit on error
set -o errexit

python -m pip install -r requirements.txt

# Collect static files for whitenoise to serve
python manage.py collectstatic --no-input

# Run migrations to build the database
python manage.py migrate
