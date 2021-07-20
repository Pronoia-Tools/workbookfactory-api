from .base import *
import dj_database_url

db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)

SECRET_KEY = os.getenv('SECRET_KEY', 'Optional default value')

SESSION_CACHE_ALIAS = "default"

DEBUG = True

ADMINS = [('Dave Merwin', 'dave@purebluedesign.com'), ]
DEFAULT_FROM_EMAIL = 'dave@purebluedesign.com'

EMAIL_HOST = 'nameserver1.bluehost.com'
EMAIL_HOST_USER = 'Sammy@WorkbookFactory.io'
EMAIL_HOST_PASSWORD = 'bui!bcR=!oT['
EMAIL_PORT = 995
EMAIL_USE_TLS = True