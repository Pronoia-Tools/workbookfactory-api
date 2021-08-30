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
    'djstripe',

    'config',
    # 'cms',
    'coaches',
    'libraries',
    'media',
    'orders',
    'users',
    'utils',
    'workbooks',
    'imagekit',

    'storages',
    'rest_framework_nested'
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
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'

# Stripe Configuration
STRIPE_LIVE_SECRET_KEY = os.environ.get("STRIPE_LIVE_SECRET_KEY", "sk_test_51JTnBaIUSxddDY4OCkqJgLEVxSJIIbRvtZ6j5n34FLdj2LEqdNJdhoCOCH0YPG2UeNJMVJV8bhWPg0ZsgspTlDFI006I0NRhvi")
STRIPE_TEST_SECRET_KEY = os.environ.get("STRIPE_TEST_SECRET_KEY", "sk_test_51JTnBaIUSxddDY4OCkqJgLEVxSJIIbRvtZ6j5n34FLdj2LEqdNJdhoCOCH0YPG2UeNJMVJV8bhWPg0ZsgspTlDFI006I0NRhvi")
STRIPE_LIVE_MODE = False  # Change to True in production
DJSTRIPE_WEBHOOK_SECRET = "whsec_xxx"  # Get it from the section in the Stripe dashboard where you added the webhook endpoint
DJSTRIPE_USE_NATIVE_JSONFIELD = True  # We recommend setting to True for new installations
DJSTRIPE_FOREIGN_KEY_TO_FIELD = "id"  # Set to `"id"` for all new 2.4+ installations

# Activate Django-Heroku.
django_on_heroku.settings(locals())