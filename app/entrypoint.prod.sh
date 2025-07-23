#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

echo "Running database migrations..."
python manage.py migrate

echo "Collecting static files..."
python manage.py collectstatic --noinput

exec "$@"