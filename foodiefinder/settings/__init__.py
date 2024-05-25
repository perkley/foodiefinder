import os
from .settings import ENVIRONMENT

if ENVIRONMENT == 'production':
    from .production import *
else:
    from .development import *