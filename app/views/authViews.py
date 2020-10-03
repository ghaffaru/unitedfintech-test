from django.shortcuts import render
from rest_framework.response import Response
# Create your views here.
from rest_framework.views import APIView

from .. import serializers
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.contrib.auth.hashers import check_password
import jwt
import environ

env = environ.Env()
# reading .env file
environ.Env.read_env()

from unitedfintech_test.mongo import db


class LoginView(APIView):

    def post(self, request):

        serializer = serializers.LoginSerializer(data=request.data)

        if serializer.is_valid():

            admin = db['admins'].find_one({'email': serializer.validated_data['email']})

            if not admin or not check_password(serializer.validated_data['password'], admin['password']):

                return Response(status=422, data={'message': 'Invalid credentials'})

            else:

                token = jwt.encode({'email': serializer.validated_data['email'],
                                    'password': admin['password']},
                                   env('JWT_KEY', default='secret'), algorithm=env('ALGO', default='HS256'))

                return Response(status=200, data={'success': True, 'token': token})

        else:

            return Response(status=422, data=serializer.errors)