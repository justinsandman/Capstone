# Authors: Justin Sandstedt, Matthew Swandal, Gabriel Morgan
#
# Web Server Gateway Interface file to ...

import os
from django.core.wsgi import get_wsgi_application

# Set the default settings module for the 'django' command.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'capstone.settings')

# Create the WSGI application object
application = get_wsgi_application()
