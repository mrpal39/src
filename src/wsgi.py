
from os import environ

from decouple import config

from django.core.wsgi import get_wsgi_application

settings_module = config("DJANGO_SETTINGS_MODULE", default="src.settings.dev")
environ["DJANGO_SETTINGS_MODULE"] = settings_module


application = get_wsgi_application()
