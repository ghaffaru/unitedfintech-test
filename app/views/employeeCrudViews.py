from rest_framework.views import APIView
from .. import serializers
from unitedfintech_test.mongo import db
from rest_framework.response import  Response

class EmployeeView(APIView):

    def post(self, request):

        serializer = serializers.EmployeeSerializer(data=request.data)

        if serializer.is_valid():

            employeeExists = db['employees'].find_one({'firstName': serializer.validated_data['firstName'],
                                      'lastName': serializer.validated_data['lastName'],
                                      'telephone': serializer.validated_data['telephone']})

            if employeeExists:
                return Response(status=422, data={'message': 'Employee already exists'})
            else:
                employee = db['employees'].insert_one({
                    'firstName': serializer.validated_data['firstName'],
                    'lastName': serializer.validated_data['lastName'],
                    'telephone': serializer.validated_data['telephone'],
                    'address': serializer.validated_data['address'],
                    'salary': serializer.validated_data['salary']
                }).inserted_id

                return Response(status=201, data={'success': True,
                                                  'employee':  serializers.EmployeeSerializer(db['employees'].find_one({'_id': employee})).data})



        else:

            return Response(status=422, data=serializer.errors)

    def get(self, request):

        employees = db['employees'].find()

        return Response(status=200, data={'employees': serializers.EmployeeSerializer(employees, many=True).data})


