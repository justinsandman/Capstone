# Authors: Justin Sandstedt, Matthew Swandal, Gabriel Morgan
#
# Python file to hold DB connection necessities.

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'my_database',  
        'USER': 'my_user',  
        'PASSWORD': 'Texasman25!', 
        'HOST': 'localhost',  
        'PORT': '3306',  # Default MySQL port
    }
}

