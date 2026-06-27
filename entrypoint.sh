#!/bin/sh

python manage.py migrate

python manage.py shell <<EOF
from django.contrib.auth import get_user_model
User = get_user_model()

username = "admin"

if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(
        username=username,
        email="admin@example.com",
        password="Admin@123"
    )
EOF

python manage.py runserver 0.0.0.0:8000