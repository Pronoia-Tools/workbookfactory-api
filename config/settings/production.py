from .base import *
import dj_database_url

db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)

SESSION_CACHE_ALIAS = "default"

DEBUG = False
ALLOWED_HOSTS = ['workbookfactory-api.herokuapp.com']