### dev.py
from .defaults import *
### other development-specific stuff



DEBUG = True
ALLOWED_HOSTS = []




STATIC_URL = '/static/'

STATICFILES_DIRS = [BASE_DIR,  "static",]
STATIC_ROOT=( BASE_DIR /'../staticfile' )
MEDIA_URL = '../media/'

# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR, "static"),
# ]

MEDIA_ROOT = ( BASE_DIR ,'../media/')



