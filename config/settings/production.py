from .base import *
import dj_database_url

db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)

SECRET_KEY = os.getenv('SECRET_KEY', 'Optional default value')

SESSION_CACHE_ALIAS = "default"

ADMINS = [('Dave Merwin', 'dave@purebluedesign.com'), ]
DEFAULT_FROM_EMAIL = 'dave@purebluedesign.com'

# EMAIL_HOST = 'nameserver1.bluehost.com'
# EMAIL_HOST_USER = 'Sammy@WorkbookFactory.io'
# EMAIL_HOST_PASSWORD = 'bui!bcR=!oT['
# EMAIL_PORT = 995
# EMAIL_USE_TLS = True

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'dave@purebluedesign.com'
EMAIL_HOST_PASSWORD = 'euzzvdprkcggqfnj'
EMAIL_PORT = 587
EMAIL_USE_TLS = True 

AWS_ACCESS_KEY_ID = "AKIAYDJD6YIFEEELVONY"
AWS_SECRET_ACCESS_KEY = "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"
AWS_STORAGE_BUCKET_NAME = "workbook-factory-dev"
AWS_S3_REGION_NAME = "us-east-2"

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': ('%(asctime)s [%(process)d] [%(levelname)s] ' +
                       'pathname=%(pathname)s lineno=%(lineno)s ' +
                       'funcname=%(funcName)s %(message)s'),
            'datefmt': '%Y-%m-%d %H:%M:%S'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        }
    },
    'handlers': {
        'null': {
            'level': 'DEBUG',
            'class': 'logging.NullHandler',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        }
    },
    'loggers': {
        'testlogger': {
            'handlers': ['console'],
            'level': 'INFO',
        }
    }
}