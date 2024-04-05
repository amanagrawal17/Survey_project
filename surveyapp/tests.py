
'''
#this is the test case for the user profile view API
# from rest_framework.test import APITestCase
# from rest_framework import status
# from django.contrib.auth import get_user_model
# from django.urls import reverse

# User = get_user_model()

# class UserProfileViewTestCase(APITestCase):
#     def setUp(self):
#         # Create a user for testing
#         self.user = User.objects.create_user(email='test@example.com', password='password123',
#                                              first_name='John', last_name='Doe')
#         self.client.force_authenticate(user=self.user)

#     def test_get_user_profile(self):
#         url = reverse('profile')  # Assuming you have configured the URL name for UserProfileView
#         response = self.client.get(url)

#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(response.data['email'], 'test@example.com')
#         self.assertEqual(response.data['first_name'], 'John')
#         self.assertEqual(response.data['last_name'], 'Doe')'''

###########################################################################################################################

'''
#this is the test case for the user register view API
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()

class UserRegisterViewTestCase(APITestCase):
    def test_user_register_view_success(self):
        url = reverse('register')  # Assuming you have configured the URL name for UserRegisterView
        data = {
            'email': 'test@example.com',
            'password': 'password123',
            'first_name': 'John',
            'last_name': 'Doe'
        }
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue('token' in response.data)
        self.assertIn('token', response.data)
        self.assertIn('msg', response.data)
        self.assertEqual(response.data['msg'], 'Registration Successfull')
        '''

# # from django.contrib.auth import get_user_model
# # from rest_framework.test import APITestCase
# # from rest_framework import status
# # from django.urls import reverse
# # from rest_framework.authtoken.models import Token
# # from .serializers import UserProfileSerializer

# # class UserProfileViewTestCase(APITestCase):
# #     def setUp(self):
# #         # Get the custom user model
# #         User = get_user_model()

# #         # Create a user and authenticate
# #         self.user = User.objects.create_user( email='test@example.com', password='password123')
# #         self.token = Token.objects.create(user=self.user)
# #         self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token.key}')
# #         self.profile_url = reverse('user-profile')

# #     def test_user_profile_view(self):
# #         # Send a GET request to the user profile endpoint
# #         response = self.client.get(self.profile_url)

# #         # Assert the response status code is 200 OK
# #         self.assertEqual(response.status_code, status.HTTP_200_OK)

# #         # Assert that the response data matches the user's profile data
# #         expected_data = UserProfileSerializer(self.user).data
# #         self.assertEqual(response.data, expected_data)





# # # from django.test import TestCase
# # # from .models import *
# # # from django.utils import timezone
# # # from rest_framework.test import APITestCase
# # # from surveyapp.serializers import *



# # # class UserLoginSerializerTestCase(TestCase):
# # #     def setUp(self):
# # #         self.user_data = {
# # #             'email': 'test@example.com',
# # #             'password': 'password123',
# # #             'first_name': 'Test',
# # #             'last_name' : 'user',
# # #             'password' : 'testpassword',
# # #             'created_at' : timezone.now(),
# # #             'updated_at' : timezone.now()
# # #         }
# # #         self.user = User.objects.create_user(**self.user_data)

# # #     def test_user_login_serializer_valid(self):
# # #         serializer = UserLoginSerializer(data=self.user_data)
# # #         self.assertTrue(serializer.is_valid())
# # #         # Validate that the serializer data matches the user data
# # #         self.assertEqual(serializer.validated_data['email'], self.user_data['email'])
# # #         self.assertEqual(serializer.validated_data['password'], self.user_data['password'])

# # #     def test_user_login_serializer_invalid(self):
# # #         # Test with missing email
# # #         invalid_data = self.user_data.copy()
# # #         invalid_data.pop('email')
# # #         print("inside the invalid function")
# # #         serializer = UserLoginSerializer(data=invalid_data)
# # #         self.assertFalse(serializer.is_valid())
# # #         # Test with missing password
# # #         invalid_data = self.user_data.copy()
# # #         invalid_data.pop('password')
# # #         serializer = UserLoginSerializer(data=invalid_data)
# # #         self.assertFalse(serializer.is_valid())









# # # # class UserRegisterSerializerTestCase(APITestCase):
# # #     # def test_user_serializer_valid_data(self):
# # #     #     data = {
# # #     #         'email': 'test@example.com',
# # #     #         'first_name': 'Test',
# # #     #         'last_name' : 'user',
# # #     #         'password' : 'testpassword',
            
# # #     #     }
# # #     #     serializer = UserRegisterSerializer(data=data)
# # #     #     self.assertTrue(serializer.is_valid())
# # #     #     self.assertEqual(serializer.errors, {})


# # #     # def test_user_serializer_create(self):
# # #     #     data = {
# # #     #         'email': 'test@example.com',
# # #     #         'first_name': 'Test',
# # #     #         'last_name' : 'user',
# # #     #         'password' : 'testpassword',
# # #     #         'created_at' : timezone.now(),
# # #     #         'updated_at' : timezone.now()
# # #     #     }
# # #     #     serializer = UserRegisterSerializer()
# # #     #     user = serializer.create(data)
# # #     #     self.assertEqual(user.email, 'test@example.com')
# # #     #     self.assertEqual(user.first_name, 'Test')
# # #     #     self.assertEqual(user.last_name, 'user')



# # # # class UserModelTest(TestCase):
# # # #     def test_create_superuser(self):
# # # #         # print ("inside test create fun")
# # # #         email = "amanagrawal1782@gmail.com"
# # # #         first_name = "Aman "
# # # #         last_name = "Agrawal"
# # # #         password = "asdf@123"
        
# # # #         superuser = User.objects.create_user(email=email, first_name=first_name, last_name=last_name, password=password, created_at=None, updated_at=None)
# # # #         # print("Userr :", user)
# # # #         self.assertEqual(superuser.email, email)
# # # #         self.assertEqual(superuser.first_name, first_name)
# # # #         self.assertEqual(superuser.last_name, last_name)
# # # #         self.assertTrue(superuser.is_active)
# # # #         self.assertFalse(superuser.is_admin)
# # # #         self.assertFalse(superuser.is_staff)
# # # #         self.assertTrue(superuser.check_password(password))
# # # #         print("test case run successfuly")

# # # # class UserMethodTest(TestCase):
# # # #     def test_has_perm(self):
# # # #         user = User(email="test@example.com")
# # # #         self.assertFalse(user.has_perm("some_permissions"))
        
# # # #     def test_is_staff(self):
# # # #         user = User(email="testemail")
# # # #         self.assertFalse(user.is_staff)

# # # # class SurveyMethodTest(TestCase):
# # # #     def test__str__(self):
# # # #         survey = Survey(s_name="testsurvey")

# # # # class Question_typesMethodTest(TestCase):
# # # #     def test__str__(self):
# # # #        q = Question_types(type="r")
# =======
from django.test import TestCase

# Create your tests here.
# >>>>>>> parent of 50ba691 (ghvghvbhj)
