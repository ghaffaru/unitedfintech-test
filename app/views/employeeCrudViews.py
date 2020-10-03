from rest_framework.views import APIView
from .. import serializers
from unitedfintech_test.mongo import db
from rest_framework.response import  Response
from bson.objectid import ObjectId
from .. import permissions
class EmployeeView(APIView):
    permission_classes = (permissions.IsAdmin,)

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



class FetchOneEmployee(APIView):
    permission_classes = (permissions.IsAdmin,)

    def get(self, request, id):

        employee = db['employees'].find_one({'_id': ObjectId(id)})
        print(employee)
        if not employee:
            return Response(status=404, data={'message': 'Not Found'})
        else:
            return Response(status=200, data={'employee': serializers.EmployeeSerializer(employee).data})


class UpdateOneEmployee(APIView):
    permission_classes = (permissions.IsAdmin,)
    def put(self, request, id):

        employee = db['employees'].find_one({'_id': ObjectId(id)})

        if not employee:
            return Response(status=404, data={'message': 'Not Found'})
        else:

            serializer = serializers.EmployeeSerializer(data=request.data)

            if serializer.is_valid():
                db['employees'].update_one({"_id": ObjectId(id)},{"$set": {
                    "firstName": serializer.validated_data['firstName'],
                    "lastName": serializer.validated_data['lastName'],
                    "address": serializer.validated_data['address'],
                    "telephone": serializer.validated_data['telephone'],
                    "salary": serializer.validated_data['salary']
                }})

                return Response(status=200, data={'success': True,
                                                  'employee': serializers.EmployeeSerializer(
                                                      db['employees'].find_one({'_id': ObjectId(id)})).data})
            else:
                return Response(status=422, data=serializer.errors)


class DeleteEmployee(APIView):
    permission_classes = (permissions.IsAdmin,)
    def delete(self, request, id):
        try:
            employee = db['employees'].find_one({'_id': ObjectId(id)})

            db['employees'].delete_one({"_id": ObjectId(id)})

            return Response(status=204)

        except:
            return Response(status=404, data={'message': 'Not Found'})

