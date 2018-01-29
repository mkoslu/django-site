from mysite.settings.base import *

DEBUG = True
INSTALLED_APPS += (
    'debug_toolbar', # and other apps for local development
)

MIDDLEWARE += ('debug_toolbar.middleware.DebugToolbarMiddleware',)

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


