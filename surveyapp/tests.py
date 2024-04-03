from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
from unittest.mock import patch
from .serializers import UserRegisterSerializer

class UserRegisterViewTestCase(APITestCase):
    def setUp(self):
        self.register_url = reverse('register')

    @patch('surveyapp.views.get_tokens_for_user')
    def test_user_register_view(self, mock_get_tokens_for_user):
        # Define the registration data
        registration_data = {
            'email': 'test@example.com',
            'password': 'password123',
            'first_name': 'Test',
            'last_name' : 'user',
            'password' : 'testpassword',
            # 'created_at' : timezone.now(),
            # 'updated_at' : timezone.now()
            # Add other required fields here
        }
        # print(registration_data)
        # Serialize the registration data
        try:
            serializer = UserRegisterSerializer(data=registration_data)
        except Exception as e:
            print ("error priny", e)
        # Validate the serializer
        self.assertTrue(serializer.is_valid())
        
        # Send a POST request to the registration endpoint
        response = self.client.post(self.register_url, registration_data, format='json')
        
        # Assert that the request was successful (status code 201)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
        # Assert that the registration response contains the expected data
        self.assertIn('token', response.data)
        self.assertIn('msg', response.data)
        self.assertEqual(response.data['msg'], 'Registration Successfull')
        
        # Assert that the get_tokens_for_user function was called
        mock_get_tokens_for_user.assert_called_once()
        
        # Assert that the user was created in the database
        self.assertTrue(User.objects.filter(email='test@example.com').exists())




# from django.test import TestCase
# from .models import *
# from django.utils import timezone
# from rest_framework.test import APITestCase
# from surveyapp.serializers import *



# class UserLoginSerializerTestCase(TestCase):
#     def setUp(self):
#         self.user_data = {
#             'email': 'test@example.com',
#             'password': 'password123',
#             'first_name': 'Test',
#             'last_name' : 'user',
#             'password' : 'testpassword',
#             'created_at' : timezone.now(),
#             'updated_at' : timezone.now()
#         }
#         self.user = User.objects.create_user(**self.user_data)

#     def test_user_login_serializer_valid(self):
#         serializer = UserLoginSerializer(data=self.user_data)
#         self.assertTrue(serializer.is_valid())
#         # Validate that the serializer data matches the user data
#         self.assertEqual(serializer.validated_data['email'], self.user_data['email'])
#         self.assertEqual(serializer.validated_data['password'], self.user_data['password'])

#     def test_user_login_serializer_invalid(self):
#         # Test with missing email
#         invalid_data = self.user_data.copy()
#         invalid_data.pop('email')
#         print("inside the invalid function")
#         serializer = UserLoginSerializer(data=invalid_data)
#         self.assertFalse(serializer.is_valid())
#         # Test with missing password
#         invalid_data = self.user_data.copy()
#         invalid_data.pop('password')
#         serializer = UserLoginSerializer(data=invalid_data)
#         self.assertFalse(serializer.is_valid())









# # class UserRegisterSerializerTestCase(APITestCase):
#     # def test_user_serializer_valid_data(self):
#     #     data = {
#     #         'email': 'test@example.com',
#     #         'first_name': 'Test',
#     #         'last_name' : 'user',
#     #         'password' : 'testpassword',
            
#     #     }
#     #     serializer = UserRegisterSerializer(data=data)
#     #     self.assertTrue(serializer.is_valid())
#     #     self.assertEqual(serializer.errors, {})


#     # def test_user_serializer_create(self):
#     #     data = {
#     #         'email': 'test@example.com',
#     #         'first_name': 'Test',
#     #         'last_name' : 'user',
#     #         'password' : 'testpassword',
#     #         'created_at' : timezone.now(),
#     #         'updated_at' : timezone.now()
#     #     }
#     #     serializer = UserRegisterSerializer()
#     #     user = serializer.create(data)
#     #     self.assertEqual(user.email, 'test@example.com')
#     #     self.assertEqual(user.first_name, 'Test')
#     #     self.assertEqual(user.last_name, 'user')



# # class UserModelTest(TestCase):
# #     def test_create_superuser(self):
# #         # print ("inside test create fun")
# #         email = "amanagrawal1782@gmail.com"
# #         first_name = "Aman "
# #         last_name = "Agrawal"
# #         password = "asdf@123"
        
# #         superuser = User.objects.create_user(email=email, first_name=first_name, last_name=last_name, password=password, created_at=None, updated_at=None)
# #         # print("Userr :", user)
# #         self.assertEqual(superuser.email, email)
# #         self.assertEqual(superuser.first_name, first_name)
# #         self.assertEqual(superuser.last_name, last_name)
# #         self.assertTrue(superuser.is_active)
# #         self.assertFalse(superuser.is_admin)
# #         self.assertFalse(superuser.is_staff)
# #         self.assertTrue(superuser.check_password(password))
# #         print("test case run successfuly")

# # class UserMethodTest(TestCase):
# #     def test_has_perm(self):
# #         user = User(email="test@example.com")
# #         self.assertFalse(user.has_perm("some_permissions"))
        
# #     def test_is_staff(self):
# #         user = User(email="testemail")
# #         self.assertFalse(user.is_staff)

# # class SurveyMethodTest(TestCase):
# #     def test__str__(self):
# #         survey = Survey(s_name="testsurvey")

# # class Question_typesMethodTest(TestCase):
# #     def test__str__(self):
# #        q = Question_types(type="r")