import dj_database_url

from .common import *

DEBUG = False
ALLOWED_HOSTS = ["todo-back-ub.herokuapp.com", "localhost", "0.0.0.0"]


DATABASES["default"] = dj_database_url.config(conn_max_age=600, ssl_require=True)
