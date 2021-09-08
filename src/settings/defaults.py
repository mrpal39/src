### default.py__
### sensible choices for default settings
from pathlib import Path
from decouple import  config
import raven


BASE_DIR = Path(__file__).resolve().parent.parent
ALLOWED_HOSTS = config("ALLOWED_HOSTS", default="")

SITE_ID=1

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',   
    "compressor",
    "corsheaders",
    "crispy_forms",
    "easy_thumbnails",
    "raven.contrib.django.raven_compat",
    "password_reset",
    "rest_framework",
    "social_django",
 
    'accounts',
   



]


MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

PROJECT_TEMPLATE_LOADERS = [
    "django.template.loaders.filesystem.Loader",
    "django.template.loaders.app_directories.Loader",
]


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': (BASE_DIR,"../templates/base.html"),
        # 'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',

                "django.contrib.auth.context_processors.auth",
                "django.template.context_processors.debug",
                "django.template.context_processors.i18n",
                "django.template.context_processors.media",
                "django.template.context_processors.static",
                "django.template.context_processors.tz",
                "django.contrib.messages.context_processors.messages",
                "social_django.context_processors.backends",
                "social_django.context_processors.login_redirect",
          
                "accounts.context_processors.users_count",            
                # "common.context_processors.analytics",

            ],
            "loaders": [("django.template.loaders.cached.Loader", PROJECT_TEMPLATE_LOADERS)],

        },
    },
]

WSGI_APPLICATION = 'src.wsgi.application'

ROOT_URLCONF = 'src.urls'
AUTH_USER_MODEL = "accounts.OwnerProfile"



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / '../db.sqlite3',
    }
}

AUTHENTICATION_BACKENDS = (
    "social_core.backends.facebook.FacebookOAuth2",
    "social_core.backends.twitter.TwitterOAuth",
    "django.contrib.auth.backends.ModelBackend",
)
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
import os
LOCALE_PATHS = [os.path.join(BASE_DIR, "../locale")]


default_email_backend = "django.core.mail.backends.console.EmailBackend"
EMAIL_USE_TLS = True
EMAIL_BACKEND = config("EMAIL_BACKEND", default=default_email_backend)
EMAIL_HOST = config("EMAIL_HOST", default="example.com")
EMAIL_PORT = config("EMAIL_PORT", default="0")
EMAIL_HOST_USER = config("EMAIL_HOST_USER", default="dummy@example.com")
EMAIL_HOST_PASSWORD = config("EMAIL_HOST_PASSWORD", default="example")

EMAIL_FILE_PATH = str(BASE_DIR.joinpath('sent_emails'))

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
    "compressor.finders.CompressorFinder",
]
COMPRESS_OFFLINE = True
THUMBNAIL_ALIASES = {
    "": {
        "pet_thumb": {"size": (350, 350), "crop": True, "upscale": True},
        "pet_poster": {"size": (550, 550), "crop": True, "upscale": True},
    }
}

THUMBNAIL_BASEDIR = "pet_thumbs"
LOGIN_URL = "accounts:login"
AUTH_USER_MODEL = "accounts.OwnerProfile"
LOGIN_REDIRECT_URL = "homepage"
LOGOUT_REDIRECT_URL = LOGIN_REDIRECT_URL


CORS_ORIGIN_ALLOW_ALL = True

REST_FRAMEWORK = {
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.LimitOffsetPagination",
    "PAGE_SIZE": 20,
}