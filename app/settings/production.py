from .common import *
import dj_database_url

DEBUG = False
ALLOWED_HOSTS = ["https://todo-uit.heroku.com"]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "todo-uit",
        "USER": "todo-uit-user",
        "PASSWORD": "todo-uit-password",
        "HOST": "localhost",
        "PORT": "5432",
    }
}


db_from_env = dj_database_url.config(conn_max_age=600)
DATABASES["default"].update(db_from_env)
