import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "skillswap.settings")
django.setup()

from accounts.models import User

# Delete all existing admin users
User.objects.filter(username='admin').delete()
User.objects.filter(email='admin@skillswap.com').delete()

# Create fresh admin with all required flags
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

print("=" * 50)
print("✅ Admin user created successfully!")
print("=" * 50)
print("Username: admin")
print("Password: admin123")
print("Email: admin@skillswap.com")
print("=" * 50)
print("🔐 Login at: http://127.0.0.1:8000/admin/")
print("=" * 50)

# Verify
print("\n🔍 Verification:")
print(f"   is_staff: {admin.is_staff}")
print(f"   is_superuser: {admin.is_superuser}")
print(f"   is_active: {admin.is_active}")
