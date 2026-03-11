"""
ASGI config for mysite project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/6.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

application = get_asgi_application()


try:
    from django.contrib.auth.models import User
    username = 'admin'
    password = 'Test123456'
    email = 'admin@example.com'

    if not User.objects.filter(username=username).exists():
        User.objects.create_superuser(username, email, password)
        print(f"✅ Superuser '{username}' created!")
    else:
        user = User.objects.get(username=username)
        user.set_password(password)
        user.save()
        print(f"🔄 Password for '{username}' updated!")
except Exception as e:
    print(f"❌ Error creating superuser: {e}")