#!/bin/sh
echo "Starting entrypoint.sh"

echo "Apply database migrations"
python manage.py migrate

echo "Collect static files"
python manage.py collectstatic --noinput

echo "Start Django Server"
python manage.py runserver 0.0.0.0:8000