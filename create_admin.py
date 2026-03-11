import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django.setup()

from django.contrib.auth.models import User

username = "admin"
email = "admin@example.com"
password = "Test123456" 

if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username, email, password)
    print(f"--- Superuser '{username}' created successfully! ---")
else:
    # ถ้ามี User นี้อยู่แล้ว ให้เปลี่ยนรหัสผ่านใหม่
    u = User.objects.get(username=username)
    u.set_password(password)
    u.save()
    print(f"--- Password for '{username}' has been updated! ---")