from django.shortcuts import render
from rest_framework.response import Response
# Create your views here.
from rest_framework.views import APIView

from . import serializers



class LoginView(APIView):

    def post(self, request):

        serializer = serializers.LoginSerializer(data=request.data)

        if serializer.is_valid():

            return Response(status=200, data={'success' : True})

        else:

            return Response(status=422, data=serializer.errors)