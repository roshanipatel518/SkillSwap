#!/usr/bin/env python
"""
Automatic superuser creation script for deployment
Runs automatically after migrations
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'skillswap.settings')
django.setup()

from accounts.models import User

# Check if any superuser exists
if not User.objects.filter(is_superuser=True).exists():
    print("Creating default superuser...")
    
    # Create default admin
    admin = User.objects.create(
        username='admin',
        email='admin@skillswap.com',
        first_name='Admin',
        last_name='User',
        role='admin',
        is_staff=True,
        is_superuser=True,
        is_active=True
    )
    admin.set_password('admin123')
    admin.save()
    
    print("=" * 60)
    print("✅ SUPERUSER CREATED SUCCESSFULLY!")
    print("=" * 60)
    print("🔐 Admin Login Credentials:")
    print("   URL: https://your-backend.onrender.com/admin/")
    print("   Username: admin")
    print("   Password: admin123")
    print("   Email: admin@skillswap.com")
    print("=" * 60)
    print("⚠️  IMPORTANT: Change password after first login!")
    print("=" * 60)
else:
    print("✓ Superuser already exists. Skipping creation.")
