from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-!-iji1-3@$w-)&gio@)xyjk1pv#ql38^-&n)9f416d&j_01yj('

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']
# if DEBUG: 
#     # Show the url to reset the password in the console.
#     EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
# else:
#     # Actually sends it to the user's email address.
#     pass

STATIC_URL = 'static/'

STATIC_ROOT = BASE_DIR / 'staticfiles'

MEDIA_URL = 'media/'

STATIC_ROOT = BASE_DIR / 'media'