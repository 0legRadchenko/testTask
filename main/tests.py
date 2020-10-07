from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase
import json

class Base(APITestCase):
    profile_list_url=reverse('all-profiles')

    def setUp(self):
        self.user = self.client.post('/auth/users/', data={'username': 'mario', 'password': 'i-keep-jumping'})
        response = self.client.post('/auth/jwt/create/', data={'username': 'mario', 'password': 'i-keep-jumping'})
        self.token = response.data['access']
        self.api_authentication()

        data = {'name': 'example1',
                'description': 'Description1',
                'location': json.dumps({"longitude": 38.975348, "latitude": 45.037295})}
        self.client.post('/api/main/companies/', data)

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)


class CompaniesTestCase(Base):

    def test_companies_insert(self):
        data = {'name': 'example',
                'description': 'Description',
                'location': json.dumps({"longitude": 38.975348, "latitude": 45.037295})}

        response = self.client.post('/api/main/companies/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_companies_list_retrieve(self):
        response = self.client.get(reverse('companies_here-list'))
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class UserProfileTestCase(Base):
    def test_profile_me(self):
        # profile_data={'user_location': json.dumps({"longitude": 38.975348, "latitude": 45.037295}),}
        response = self.client.get('/auth/users/me/')
        print(response, response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_userprofile_list_authenticated(self):
        response=self.client.get(self.profile_list_url)
        self.assertEqual(response.status_code,status.HTTP_200_OK)

    def test_userprofile_list_unauthenticated(self):
        self.client.force_authenticate(user=None)
        response=self.client.get(self.profile_list_url)
        self.assertEqual(response.status_code,status.HTTP_401_UNAUTHORIZED)