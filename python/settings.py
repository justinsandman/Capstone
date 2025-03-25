# Authors: Justin Sandstedt, Matthew Swandal, Gabriel Morgan
#
# Python file to hold DB connection necessities.

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'my_database',  # DB name
        'USER': 'my_user',  #  PostgreSQL username
        'PASSWORD': 'mypassword',  #  PostgreSQL password
        'HOST': 'localhost',  # Since its running locally
        'PORT': '5432',  # Default PostgreSQL port
    }
}
