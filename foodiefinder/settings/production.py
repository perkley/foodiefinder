from .settings import *

print("Production Settings Applied")

STATIC_ROOT = '/home/ubuntu/foodiefinder/static'

SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
