#!/bin/bash
# Build script for deployment

set -e  # Exit on error

echo "Installing dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

echo "Collecting static files..."
python manage.py collectstatic --no-input --clear

echo "Running migrations..."
python manage.py migrate --no-input

echo "Creating superuser..."
python create_superuser.py || echo "Superuser creation skipped"

echo "Build completed successfully!"
