release: python manage.py migrate
release: python manage.py createsuperuser --username admin --password admin
web: gunicorn app.wsgi
heroku config:set DEBUG_COLLECTSTATIC=1