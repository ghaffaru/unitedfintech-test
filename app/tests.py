from django.test import TestCase
from rest_framework.test import APIClient, APITestCase
# Create your tests here.
from rest_framework.test import RequestsClient
from unitedfintech_test.mongo import db
from django.contrib.auth.hashers import make_password
class HomeTest(TestCase):

    def setUp(self):
        self.client = APIClient()

    def test_home_works(self):

        response = self.client.get('')

        self.assertEqual(response.status_code, 200)


class AdminTest(APITestCase):

    def test_admin_can_signin(self):

        db['admins'].insert_one({
            'name': 'Ghaff',
            'email': 'ghaff@gmail.com',
            'password': make_password('12345678')
        })

        response = self.client.post('/api/login', {'email': 'ghaff@gmail.com', 'password': '12345678'}, format='json')

        self.assertEqual(response.status_code, 200)

class EmployeeCrudTest(APITestCase):

    def setUp(self):

        self.client = APIClient()

        # Clear DB
        db['admins'].delete_many({})
        db['employees'].delete_many({})


        db['admins'].insert_one({
            'name': 'Ghaff',
            'email': 'ghaff@gmail.com',
            'password': make_password('12345678')
        })

        response = self.client.post('/api/login', {'email': 'ghaff@gmail.com', 'password': '12345678'}, format='json')

        self.token = response.json()    ['token']


    def test_admin_can_add_new_employee(self):

      data = {
            'firstName': 'first Name',
            'lastName': 'last Name',
            'telephone': '0254242424',
            'address': 'Accra',
            'salary': 2888
        }
      self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)
      response = self.client.post('/api/employee', data)

      self.assertEqual(response.status_code, 201)


    def test_admin_can_view_one_employee(self):
        data = {
            'firstName': 'first Name',
            'lastName': 'last Name',
            'telephone': '0254242424',
            'address': 'Accra',
            'salary': 2888
        }
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)
        response = self.client.post('/api/employee', data)

        response2 = self.client.get('/api/employee/' +response.json()['employee']['_id'])

        self.assertEqual(response2.status_code, 200)

    def test_admin_can_update_one_employee(self):
        data = {
            'firstName': 'first Name',
            'lastName': 'last Name',
            'telephone': '0254242424',
            'address': 'Accra',
            'salary': 2888
        }

        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)
        response = self.client.post('/api/employee', data)

        id = response.json()['employee']['_id']
        new_data = {
            'firstName': 'first Name Updated',
            'lastName': 'last Name',
            'telephone': '0254242424',
            'address': 'Accra',
            'salary': 288
        }
        response2 = self.client.put('/api/employeeUpdate/' + id , new_data)

        self.assertEqual(response2.json()['employee']['firstName'], new_data['firstName']) # basic assertion

    def test_admin_can_delete_an_employee(self):
        data = {
            'firstName': 'first Name',
            'lastName': 'last Name',
            'telephone': '0254242424',
            'address': 'Accra',
            'salary': 2888
        }

        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)
        response = self.client.post('/api/employee', data)


        response2 = self.client.delete('/api/employeeDelete/' + response.json()['employee']['_id'])

        self.assertEqual(response2.status_code, 204)