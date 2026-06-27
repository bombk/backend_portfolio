#!/bin/sh

echo "Running migrations..."
python manage.py migrate

echo "Creating superuser if not exists..."

python manage.py shell <<EOF
from django.contrib.auth import get_user_model
import os

User = get_user_model()

username = os.getenv("DJANGO_SUPERUSER_USERNAME", "admin")
email = os.getenv("DJANGO_SUPERUSER_EMAIL", "admin@example.com")
password = os.getenv("DJANGO_SUPERUSER_PASSWORD", "Admin@123")

if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(
        username=username,
        email=email,
        password=password
    )
    print("Superuser created:", username)
else:
    user = User.objects.get(username=username)
    user.is_staff = True
    user.is_superuser = True
    user.save()
    print("Superuser already exists:", username)
EOF

echo "Starting Django..."
python manage.py runserver 0.0.0.0:8000