release: python manage.py migrate
heroku config:set DJANGO_SUPERUSER_USERNAME=admin
heroku config:set DJANGO_SUPERUSER_PASSWORD=admin
heroku config:set DJANGO_SUPERUSER_EMAIL=admin@monos.mn
release: python manage.py createsuperuser --no-input
web: gunicorn app.wsgi
heroku config:set DEBUG_COLLECTSTATIC=1