# Authors: Justin Sandstedt, Matthew Swandal, Gabriel Morgan
#
# Python file to hold DB connection necessities.

DATABASES = {
    'default': {
        'ENGINE': '', #django.db.backends.mysql
        'NAME': 'userlog',
        'USER': 'optiplex 7070',
        'PASSWORD': '',
        'HOST': 'instance-ip',
        'PORT': '3306',
    }
}