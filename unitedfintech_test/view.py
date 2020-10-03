from rest_framework.response import Response
from rest_framework.views import APIView


class Home(APIView):

    def get(self, request):

        return Response(status=200, data={'message': 'Employee API is running'})