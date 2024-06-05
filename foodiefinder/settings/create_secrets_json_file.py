import json
from django.conf import settings
import os
from django.core.management.utils import get_random_secret_key

def create_initial_secrets_json_file(filename, environment):
    secret_key = get_random_secret_key()
    
    if environment == 'development':
        secrets = {
            "SECRET_KEY": secret_key,
            "DEBUG": "True",
            "ALLOWED_HOSTS": ["localhost"],
            "AWS_COGNITO_USER_POOL_ID": "",
            "AWS_COGNITO_APP_CLIENT_ID": "",
            "AWS_COGNITO_APP_CLIENT_SECRET": "",
            "AWS_COGNITO_REGION": "",
            "AWS_COGNITO_URL": "",
            "AWS_COGNITO_LOGIN_REDIRECT_URL": "",
            "AWS_COGNITO_LOGOUT_REDIRECT_URL": ""
        }
    else:
        secrets = {
            "SECRET_KEY": secret_key,
            "AWS_SECRETS_MANAGER_NAME": ""
        }
    with open(filename, 'w') as secrets_file:
        json.dump(secrets, secrets_file, indent=2)

    print("Secret key has been written to secrets.json")
