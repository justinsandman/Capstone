"""
WSGI configuration for our Capstone project. 

Authors: Justin Sandstedt, Matthew Swandal, Gabriel Morgan

This file exposes the WSGI callable as a module-level variable named 'application'.
It is used by WSGI-compatible web servers to serve your project.

For more information on this file, see ... 
"""
import os
from django.core.wsgi import get_wsgi_application

# Set the default settings module for the 'django' command.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'capstone.settings')

# Create the WSGI application instance
application = get_wsgi_application()
