from rest_framework.permissions import BasePermission
from rest_framework.authtoken.models import Token
from rest_framework import permissions
from rest_framework.exceptions import AuthenticationFailed
import jwt
from unitedfintech_test.mongo import db
import environ

env = environ.Env()

environ.Env.read_env()

class IsAdmin(BasePermission):

    def has_permission(self, request, view):

        if 'Authorization' in request.headers:
            token = request.headers['Authorization'].split(' ')[-1]

            try:

                decoded = jwt.decode(token,  env('JWT_KEY', default='secret'), algorithm=env('ALGO', default='HS256'))
                print(decoded)
                if not db['admins'].find_one({'email': decoded['email'], 'password': decoded['password']}):
                    return False
                else:
                    return True
            except:
                raise AuthenticationFailed('Invalid Token')
        else:
            return False