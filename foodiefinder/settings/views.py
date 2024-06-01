# views.py
from django.http import JsonResponse
from django.shortcuts import redirect
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth import login, logout
import requests
import urllib.parse
import jwt

def cognito_login(request):
    base_url = f"{settings.AWS_COGNITO_URL}/login"
    params = {
        'client_id': settings.AWS_COGNITO_APP_CLIENT_ID,
        'response_type': 'code',
        'scope': 'openid profile email',
        'redirect_uri': settings.AWS_COGNITO_LOGIN_REDIRECT_URL,
    }
    url = f"{base_url}?{urllib.parse.urlencode(params)}"
    return redirect(url)

def cognito_callback(request):
    code = request.GET.get('code')
    if not code:
        return JsonResponse({'error': 'Authorization code not provided'}, status=400)

    token_url = f"{settings.AWS_COGNITO_URL}/oauth2/token"
    data = {
        'grant_type': 'authorization_code',
        'client_id': settings.AWS_COGNITO_APP_CLIENT_ID,
        'redirect_uri': settings.AWS_COGNITO_LOGIN_REDIRECT_URL,
        'code': code,
    }
    if settings.AWS_COGNITO_APP_CLIENT_SECRET:
        auth = (settings.AWS_COGNITO_APP_CLIENT_ID, settings.AWS_COGNITO_APP_CLIENT_SECRET)
    else:
        auth = None

    response = requests.post(token_url, data=data, auth=auth)
    tokens = response.json()

    if 'error' in tokens:
        return JsonResponse(tokens, status=400)

    # Store tokens in session or return them in response
    request.session['id_token'] = tokens.get('id_token')
    request.session['access_token'] = tokens.get('access_token')
    request.session['refresh_token'] = tokens.get('refresh_token')

    claims = decode_jwt(request.session['id_token'], settings.AWS_COGNITO_REGION, settings.AWS_COGNITO_USER_POOL_ID, settings.AWS_COGNITO_APP_CLIENT_ID)

    # Setup User
    User = get_user_model()
    # cognito_sub = user_info['sub']
    username = claims['cognito:username']
    email = claims['email']
    fName = claims['given_name']
    lName = claims['family_name']

    #print(User.objects.filter(email=claims['email']).query)
    user, created = User.objects.get_or_create(defaults={'first_name': fName, 'last_name': lName}, email=email)
    if not created:
        user.username = username
        user.email = email
        user.first_name = fName
        user.last_name = lName
        user.save()

    login(request, user)  # Log in the user

    return redirect('/')  # Redirect to your desired page after login


def cognito_signup(request):
    base_url = f"{settings.AWS_COGNITO_URL}/signup"
    params = {
        'client_id': settings.AWS_COGNITO_APP_CLIENT_ID,
        'response_type': 'code',
        'scope': 'openid profile email',
        'redirect_uri': settings.AWS_COGNITO_LOGIN_REDIRECT_URL,
    }
    url = f"{base_url}?{urllib.parse.urlencode(params)}"
    return redirect(url)

def cognito_logout(request):
    
    # Log out from Django
    logout(request)

    # Prepare the Cognito logout URL
    base_url = f"{settings.AWS_COGNITO_URL}/logout"
    params = {
        'client_id': settings.AWS_COGNITO_APP_CLIENT_ID,
        'logout_uri': settings.AWS_COGNITO_LOGOUT_REDIRECT_URL,
    }
    logout_url = f"{base_url}?{urllib.parse.urlencode(params)}"

    return redirect(logout_url)


def get_jwks(region, user_pool_id):
    url = f'https://cognito-idp.{region}.amazonaws.com/{user_pool_id}/.well-known/jwks.json'
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

def decode_jwt(token, region, user_pool_id, app_client_id):
    jwks = get_jwks(region, user_pool_id)
    header = jwt.get_unverified_header(token)
    key = next(k for k in jwks['keys'] if k['kid'] == header['kid'])
    public_key = jwt.algorithms.RSAAlgorithm.from_jwk(key)
    return jwt.decode(token, public_key, audience=app_client_id, algorithms=['RS256'])