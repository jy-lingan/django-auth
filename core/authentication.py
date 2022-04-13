import datetime
import jwt
from .models import User
from rest_framework import exceptions
from rest_framework.authentication import get_authorization_header
#from rest_framework.response import Response
from rest_framework.authentication import BaseAuthentication
from .serializers import UserSerializer


class JWTAuthentication(BaseAuthentication):
    def authenticate(self, request):
        auth = get_authorization_header(request).split()

        if auth and len(auth) == 2:
            token = auth[1].decode('utf-8')
            id = decode_access_token(token)

            user = User.objects.get(pk=id)

            return (user, None)

        raise exceptions.AuthenticationFailed('Invalid credentials')


def create_access_token(id):
    return jwt.encode({
        'user_id': id,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=60),
        'iat': datetime.datetime.utcnow()
    }, 'access_token', algorithm='HS256')


def decode_access_token(token):
    try:
        payload = jwt.decode(token, 'access_token', algorithms='HS256')

        return payload['user_id']
    except:
        raise exceptions.AuthenticationFailed('Invalid token')


def create_refresh_token(id):
    return jwt.encode({
        'user_id': id,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(days=7),
        'iat': datetime.datetime.utcnow()
    }, 'refresh_token', algorithm='HS256')


def decode_refresh_token(token):
    try:
        payload = jwt.decode(token, 'refresh_token', algorithms='HS256')

        return payload['user_id']
    except:
        raise exceptions.AuthenticationFailed('Invalid token')
