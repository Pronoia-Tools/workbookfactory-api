import os
from pathlib import Path
import django_on_heroku

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

AUTH_USER_MODEL = "users.Account"
LOGIN_URL = '/accounts/login/'
ADMIN_URL = "workbook-factory/admin/"
# LOGIN_REDIRECT_URL = "/app/"

DATE_FORMAT = "d/m/Y"
DATE_INPUT_FORMATS = ('%m/%d/%Y',)

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.sites',
    'django.contrib.staticfiles',

    'wagtail.contrib.forms',
    'wagtail.contrib.redirects',
    'wagtail.embeds',
    'wagtail.sites',
    'wagtail.users',
    'wagtail.snippets',
    'wagtail.documents',
    'wagtail.images',
    'wagtail.search',
    'wagtail.admin',
    'wagtail.core',

    'modelcluster',
    'taggit',
    'taggit_serializer',

    'rest_framework',
    'rest_framework.authtoken',

    'dj_rest_auth',
    'allauth',
    'allauth.account',
    'dj_rest_auth.registration',
    'allauth.socialaccount',

    'corsheaders',

    'django_countries',
    'djmoney',

    'config',
    # 'cms',
    'coaches',
    'libraries',
    'media',
    'orders',
    'users',
    'utils',
    'workbooks',
]

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'

MIDDLEWARE = (
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'wagtail.contrib.redirects.middleware.RedirectMiddleware',
)

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates'), ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'

SITE_ID = 1


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Allauth settings
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = 'none'
ACCOUNT_AUTHENTICATION_METHOD = "email"
ACCOUNT_SIGNUP_FORM_CLASS = 'users.forms.SignupForm'

REST_USE_JWT = True
JWT_AUTH_COOKIE = 'workbookfactory-auth'
JWT_AUTH_REFRESH_COOKIE = 'workbookfactory-refresh-token'

# Rest Framework Settings
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ]
}

REST_AUTH_SERIALIZERS = {
    'USER_DETAILS_SERIALIZER': 'users.api.serializers.AccountSerializer',
}

REST_AUTH_REGISTER_SERIALIZERS = {
    'REGISTER_SERIALIZER': 'users.api.serializers.CustomRegisterSerializer',
}


# CORS
CORS_ALLOW_ALL_ORIGINS = True
# CORS_ALLOWED_ORIGINS = [
#    "https://workbookfactory-api.herokuapp.com/",
#    "https://workbook-factory.herokuapp.com/",
#    "http://localhost:8000",
#    "http://127.0.0.1:8000"
#]


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, os.pardir, 'static'),
]

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, os.pardir, 'static')

MEDIA_ROOT = os.path.join(BASE_DIR, os.pardir, 'uploads')
MEDIA_URL = '/uploads/'

FILE_UPLOAD_PERMISSIONS = 0o644

WAGTAIL_SITE_NAME = 'Workbook Factory'
# WAGTAILIMAGES_IMAGE_MODEL = 'cms.CustomImage'
# PASSWORD_REQUIRED_TEMPLATE = 'account/login.html'
WAGTAIL_FRONTEND_LOGIN_URL = '/accounts/login/'

# AWS Credentials
AWS_ACCESS_KEY_ID = 'AKIAYDJD6YIFEEELVONY'
AWS_SECRET_ACCESS_KEY = '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'
AWS_STORAGE_BUCKET_NAME = 'workbook-factory-dev'
AWS_S3_REGION_NAME = 'us-east-2'
AWS_S3_ENDPOINT_URL = 'https://s3.us-east-2.amazonaws.com'

S3DIRECT_DESTINATIONS = {
    'primary_destination': {
        'key': 'uploads/',
        'allowed': ['image/jpg', 'image/jpeg', 'image/png', 'video/mp4'],
    }
}
# Activate Django-Heroku.
django_on_heroku.settings(locals())