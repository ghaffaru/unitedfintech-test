from django.shortcuts import render
from rest_framework.response import Response
# Create your views here.
from rest_framework.views import APIView

from . import serializers
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

class LoginView(APIView):

    def post(self, request):

        serializer = serializers.LoginSerializer(data=request.data)

        if serializer.is_valid():
            admin = User.objects.filter(username=serializer.validated_data['username']).first()

            if not admin or not admin.check_password(serializer.validated_data['password']):

                return Response(status=422, data={'message': 'Invalid credentials'})
            else:

                token, created = Token.objects.get_or_create(user=admin)

                return Response(status=200, data={'success' : True, 'token': token.key})

        else:

            return Response(status=422, data=serializer.errors)