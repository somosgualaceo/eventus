from .base import *

DEBUG = False
TEMPLATE_DEBUG = False
ALLOWED_HOSTS = ['*']


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'db3eu4d15pjse2',
        'USER': 'lrddzzyakupmxa',
        'PASSWORD': 'O0AmLiuN4AkJqOd0ThYgTkBH6m',
        'HOST': 'ec2-54-221-201-165.compute-1.amazonaws.com',
        'PORT': '5432',
    }
}

STATIC_URL = '/static/'
STATIC_ROOT = 'staticfiles'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR.child('media')