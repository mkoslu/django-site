from mysite.settings.base import *

DEBUG = False
INSTALLED_APPS += (
    # other apps for production site
)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'memet$mysite',
        'USER': 'memet',
        'HOST': 'memet.mysql.pythonanywhere-services.com',
    }
}
