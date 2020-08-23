from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'u8od8lr1b18-zmz^gpv*7hg+xt5fgyr$cr8r#nr43a2jajd*12'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
