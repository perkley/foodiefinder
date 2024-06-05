from .settings import *

print("Development Settings Applied")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = get_local_secret('DEBUG').lower() == 'true'

#allowed_hosts_str = get_local_secret('ALLOWED_HOSTS')
ALLOWED_HOSTS = get_local_secret('ALLOWED_HOSTS')

AWS_COGNITO_USER_POOL_ID = get_local_secret('AWS_COGNITO_USER_POOL_ID')
AWS_COGNITO_APP_CLIENT_ID = get_local_secret('AWS_COGNITO_APP_CLIENT_ID')
AWS_COGNITO_APP_CLIENT_SECRET = get_local_secret('AWS_COGNITO_APP_CLIENT_SECRET')
AWS_COGNITO_REGION = get_local_secret('AWS_COGNITO_REGION')
AWS_COGNITO_URL = get_local_secret('AWS_COGNITO_URL')
AWS_COGNITO_LOGIN_REDIRECT_URL = get_local_secret('AWS_COGNITO_LOGIN_REDIRECT_URL')
AWS_COGNITO_LOGOUT_REDIRECT_URL = get_local_secret('AWS_COGNITO_LOGOUT_REDIRECT_URL')