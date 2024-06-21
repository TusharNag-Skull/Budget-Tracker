"""
WSGI config for budget_tracker project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os #import os module

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "budget_tracker.settings")
#defining the setting module to environment variable
#os.environment.setdefault this used as
# "A mapping object representing the string environment"
application = get_wsgi_application() #This functions returns the WSGI callable
#Here the application is callable Object