# Authors: Justin Sandstedt, Matthew Swandal, Gabriel Morgan
#
# Python file to hold DB connection necessities.

DATABASES = {
    'default': {
<<<<<<< HEAD
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'my_database',  # DB name
        'USER': 'my_user',  #  PostgreSQL username
        'PASSWORD': 'mypassword',  #  PostgreSQL password
        'HOST': 'localhost',  # Since its running locally
        'PORT': '5432',  # Default PostgreSQL port
=======
        'ENGINE': '', #django.db.backends.mysql
        'NAME': 'userlog',
        'USER': 'optiplex 7070',
        'PASSWORD': '',
        'HOST': 'instance-ip',
        'PORT': '3306',
>>>>>>> c31e8ea77f856a2e2bcf68516a29f0bc5334f50b
    }
}
