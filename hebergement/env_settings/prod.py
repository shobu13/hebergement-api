from .settings import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['hebergement-api.shobu.fr']

DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': 'hebergement',
        'HOST': 'shobu.fr',
        'PORT': 27018,
        'USER': 'mongoadmin',
        'PASSWORD': 'Jioshield13#Saucisse'
    }

    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': os.path.join(BASE_DIR, 'db.sqlite3')
    # }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

STATIC_ROOT = os.path.join("/var/www/hebergement", "static")
MEDIA_ROOT = os.path.join("/var/www/hebergement", "media")
MEDIA_URL = '/media/'
