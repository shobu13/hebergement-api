from ..settings import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': 'hebergement',
        'HOST': 'shobu.fr',
        'PORT': 27018,
        'USER': 'mongoadmin',
        'PASSWORD': 'Jioshield13#Saucisse'
    }
}
