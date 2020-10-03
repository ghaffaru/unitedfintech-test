from rest_framework import serializers

class LoginSerializer(serializers.Serializer):

    email = serializers.CharField(required=True
                                     )

    password = serializers.CharField(required=True)

class EmployeeSerializer(serializers.Serializer):

    firstName = serializers.CharField(required=True
                                      )

    lastName = serializers.CharField(required=True)

    telephone = serializers.CharField(required=True)

    address = serializers.CharField(required=True)

    salary = serializers.FloatField(required=True)



