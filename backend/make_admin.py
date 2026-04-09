#!/usr/bin/env python
import os
import sys

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'skillswap.settings')
import django
django.setup()

from accounts.models import User

# Delete existing
try:
    User.objects.filter(username='myadmin').delete()
    print("Deleted old admin")
except:
    pass

# Create new
admin = User.objects.create(
    username='myadmin',
    email='myadmin@test.com',
    first_name='My',
    last_name='Admin',
    role='admin',
    is_staff=True,
    is_superuser=True,
    is_active=True
)
admin.set_password('admin123')
admin.save()

print("\n" + "="*60)
print("SUCCESS! Admin created!")
print("="*60)
print("Username: myadmin")
print("Password: admin123")
print("URL: http://127.0.0.1:8000/admin/")
print("="*60)
