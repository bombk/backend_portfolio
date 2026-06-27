#!/bin/sh

echo "Starting application..."

# check sqlite exists
if [ -f "/app/db.sqlite3" ]; then
    echo "Using existing SQLite database: /app/db.sqlite3"
else
    echo "WARNING: db.sqlite3 not found"
fi

exec python manage.py runserver 0.0.0.0:8000