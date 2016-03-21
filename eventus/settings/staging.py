from .base import *

DEBUG = False
TEMPLATE_DEBUG = False
ALLOWED_HOSTS = ['*']


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'dbscdafnm42f22',
        'USER': 'hpknqfswmpmajs',
        'PASSWORD': '-hPr2z8Pq2YLHagehdoA0NOUPl',
        'HOST': 'ec2-107-22-248-209.compute-1.amazonaws.com',
        'PORT': '5432',
    }
}

STATIC_URL = '/static/'
STATIC_ROOT = 'staticfiles'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR.child('media')