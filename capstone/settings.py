"""
Django settings for our capstone project. 

This file contains configuration settings for the entire web applciation, 
including database setup, installed apps, middleware, templates, and static files.

Authors: 
For more information on this file, see: 
"""
from pathlib import Path  # For handling our filesystem paths in an OS- independent way 

# BASE_DIR is root directory of the project. 
BASE_DIR = Path(__file__).resolve().parent.parent  

# SECURITY WARNING: keep this secret upon entering production. 
SECRET_KEY = '52495'  

# SECURITY WARNING: DO NOT RUN WITH DEBUG ON IN PRODUCTION. 
DEBUG = True  # Change to False in production

# Valid host/domain names for our site.
ALLOWED_HOSTS = ['localhost', '127.0.0.1']

# Application definition 
INSTALLED_APPS = [
    # Default Django apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Custom apps
    'capstone',  # Main app 
    'core',      # Handles base logic  
    'nutrition', # Contains models to DB 
]


# Middleware is a framework that ...
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Entry point for root URL config
ROOT_URLCONF = 'capstone.urls'  # project name

# Template config - defines how Django loads HTML templates.
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # Template directory 
        'APP_DIRS': True, # Searches for templates in app-specific directories
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# WSGI config for production deployments 
WSGI_APPLICATION = 'capstone.wsgi.application'  # project name

# Database config
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # MySQL backend
        'NAME': 'my_database',                # DB name 
        'USER': 'root',                       # DB User 
        'PASSWORD': 'Texasman25!',            # DB PW (Change in prodcution)
        'HOST': 'localhost',                  # DB Host 
        'PORT': '3306',                       # Default MySQL port
    }
}


# Default primary key field type 
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Password valdiation to enforce stronger password policies. 
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Internationalization settings 
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Logo)
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']  # Path

# Directory where collectstatic will collect static files to show images
STATIC_ROOT = BASE_DIR / 'staticfiles'  # Used to store the static files after running collectstatic