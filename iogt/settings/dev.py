from .base import *

# Development Applications not passed into production
INSTALLED_APPS += [
    'wagtail.api.v2',
    'rest_framework',
]
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'jjfayj6d=90@@@(rop$98ryt36vuyf3!chtneyoku3_f)*z^h_'

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ['*']

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


try:
    from .local import *
except ImportError:
    pass
