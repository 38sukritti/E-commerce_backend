#!/usr/bin/env bash
# exit on error
set -o errexit

python -m pip install -r requirements.txt

# Run migrations to build the database
python manage.py migrate
