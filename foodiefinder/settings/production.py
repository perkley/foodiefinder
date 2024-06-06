from .settings import *
import boto3
import json
from django.core.exceptions import ImproperlyConfigured

print("Production Settings Applied")

STATIC_ROOT = '/home/ubuntu/foodiefinder/static'

SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

def get_aws_secret(secret_name):
    # Create a Secrets Manager client
    session = boto3.session.Session()
    client = boto3.client('secretsmanager', region_name='us-east-1')

    try:
        
        get_secret_value_response = client.get_secret_value(SecretId=secret_name)
    except Exception as e:
        # For a list of exceptions thrown, see
        # https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_GetSecretValue.html
        raise ImproperlyConfigured(f"Error retrieving secret {secret_name}: {e}")

    # Decrypts secret using the associated KMS key
    secret = get_secret_value_response['SecretString']
    return json.loads(secret)


# Fetch your secret values
aws_secrets_manager_name = get_local_secret('AWS_SECRETS_MANAGER_NAME')
secrets = get_aws_secret(aws_secrets_manager_name)

DEBUG = secrets['Debug'].lower() == 'true'

allowed_hosts_str = secrets['AllowedHosts']
ALLOWED_HOSTS = allowed_hosts_str.split(',')

AWS_COGNITO_USER_POOL_ID = secrets['UserPoolId']
AWS_COGNITO_APP_CLIENT_ID = secrets['ClientId']
AWS_COGNITO_APP_CLIENT_SECRET = secrets['ClientSecret']
AWS_COGNITO_REGION = secrets['Region']
AWS_COGNITO_URL = secrets['CognitoUrl']
AWS_COGNITO_LOGIN_REDIRECT_URL = secrets['CognitoLoginRedirectUrl']
AWS_COGNITO_LOGOUT_REDIRECT_URL = secrets['CognitoLogoutRedirectUrl']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': secrets['RdsDatabaseName'],
        'USER': secrets['RdsUser'],
        'PASSWORD': secrets['RdsPassword'],
        'HOST': secrets['RdsHost'],
        'PORT': secrets['RdsPort'], 
    }
}