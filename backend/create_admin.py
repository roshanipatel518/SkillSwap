import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "skillswap.settings")
django.setup()

from accounts.models import User

# Delete existing admin if exists
User.objects.filter(email='admin@skillswap.com').delete()

# Create new admin
admin = User.objects.create_superuser(
    username='admin',
    email='admin@skillswap.com',
    password='admin123',
    first_name='Admin',
    last_name='User',
    role='admin'
)

print("✅ Admin user created successfully!")
print("   Email: admin@skillswap.com")
print("   Username: admin")
print("   Password: admin123")
print("\n🔐 Django Admin Panel: http://127.0.0.1:8000/admin/")
