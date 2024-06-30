#!/bin/sh -x
python manage.py migrate
python manage.py collectstatic
cp -rg /app/static/ . /backend_static/static/
gunicorn --bind 0.0.0.0:8000 config.wsgi
