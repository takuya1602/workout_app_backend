from .settings_common import *
import os
import dj_database_url

SECRET_KEY = os.environ["SECRET_KEY"]

DEBUG = False

ALLOWED_HOSTS = ["*"]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ["DB_NAME"],
        "USER": os.environ["DB_USER"],
        "PASSWORD": os.environ["DB_PASSWORD"],
        "HOST": os.environ["DB_POST"],
        "PORT": os.environ["DB_PORT"],
    }
}

db_from_env = dj_database_url.config(conn_max_age=600, ssl_require=True)
DATABASES["default"].update(db_from_env)
