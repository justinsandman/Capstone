# Authors: Justin Sandstedt, Matthew Swandal, Gabriel Morgan
#
# Python file to hold DB connection necessities.

DATABASES = {
    'default': {
        'ENGINE': '', #django.db.backends.mysql
        'NAME': 'database_name',
        'USER': 'username',
        'PASSWORD': 'password',
        'HOST': 'instance-ip',
        'PORT': '3306',
    }
}