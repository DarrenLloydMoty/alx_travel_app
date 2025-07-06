import os
import environ
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent


# Initialize environment variables
env = environ.Env(
    DEBUG=(bool, False)
)

# Read the .env file
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env('DEBUG')

# Installed apps (add these)
INSTALLED_APPS = [
    # other apps...
    'rest_framework',
    'corsheaders',
    'drf_yasg',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',  # add at the top of middleware list
    # other middleware...
    'django.middleware.common.CommonMiddleware',
    # ...
]

# CORS settings: allow all origins or specify
CORS_ALLOWED_ORIGINS = [
    # example:
    "http://localhost:3000",
    # add your frontend URLs here
]

# or to allow all origins (not recommended for production)
# CORS_ALLOW_ALL_ORIGINS = True

# REST Framework basic config (customize as needed)
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ),
}

# Database configuration for MySQL using environ
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': env('MYSQL_DB_NAME'),
        'USER': env('MYSQL_USER'),
        'PASSWORD': env('MYSQL_PASSWORD'),
        'HOST': env('MYSQL_HOST'),
        'PORT': env('MYSQL_PORT'),
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        },
    }
}
