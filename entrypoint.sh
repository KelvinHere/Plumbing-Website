#!/bin/sh

# Wait for postgres
if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

# Script
python manage.py flush --no-input
python manage.py makemigrations --no-input
python manage.py makemigrations products --no-input
python manage.py migrate --no-input
python manage.py ensure_initial_users
python manage.py loaddata brands.json
python manage.py loaddata shops.json
python manage.py loaddata categories.json
python manage.py loaddata products.json

exec "$@"