from django.test import TestCase
from .models import *
from django.utils import timezone
from rest_framework.test import APITestCase
from surveyapp.serializers import *



class UserLoginSerializerTestCase(TestCase):
    def setUp(self):
        self.user_data = {
            'email': 'test@example.com',
            'password': 'password123',
            'first_name': 'Test',
            'last_name' : 'user',
            'password' : 'testpassword',
            'created_at' : timezone.now(),
            'updated_at' : timezone.now()
        }
        self.user = User.objects.create_user(**self.user_data)

    def test_user_login_serializer_valid(self):
        serializer = UserLoginSerializer(data=self.user_data)
        self.assertTrue(serializer.is_valid())
        # Validate that the serializer data matches the user data
        self.assertEqual(serializer.validated_data['email'], self.user_data['email'])
        self.assertEqual(serializer.validated_data['password'], self.user_data['password'])





















# class UserRegisterSerializerTestCase(APITestCase):
    # def test_user_serializer_valid_data(self):
    #     data = {
    #         'email': 'test@example.com',
    #         'first_name': 'Test',
    #         'last_name' : 'user',
    #         'password' : 'testpassword',
            
    #     }
    #     serializer = UserRegisterSerializer(data=data)
    #     self.assertTrue(serializer.is_valid())
    #     self.assertEqual(serializer.errors, {})


    # def test_user_serializer_create(self):
    #     data = {
    #         'email': 'test@example.com',
    #         'first_name': 'Test',
    #         'last_name' : 'user',
    #         'password' : 'testpassword',
    #         'created_at' : timezone.now(),
    #         'updated_at' : timezone.now()
    #     }
    #     serializer = UserRegisterSerializer()
    #     user = serializer.create(data)
    #     self.assertEqual(user.email, 'test@example.com')
    #     self.assertEqual(user.first_name, 'Test')
    #     self.assertEqual(user.last_name, 'user')



# class UserModelTest(TestCase):
#     def test_create_superuser(self):
#         # print ("inside test create fun")
#         email = "amanagrawal1782@gmail.com"
#         first_name = "Aman "
#         last_name = "Agrawal"
#         password = "asdf@123"
        
#         superuser = User.objects.create_user(email=email, first_name=first_name, last_name=last_name, password=password, created_at=None, updated_at=None)
#         # print("Userr :", user)
#         self.assertEqual(superuser.email, email)
#         self.assertEqual(superuser.first_name, first_name)
#         self.assertEqual(superuser.last_name, last_name)
#         self.assertTrue(superuser.is_active)
#         self.assertFalse(superuser.is_admin)
#         self.assertFalse(superuser.is_staff)
#         self.assertTrue(superuser.check_password(password))
#         print("test case run successfuly")

# class UserMethodTest(TestCase):
#     def test_has_perm(self):
#         user = User(email="test@example.com")
#         self.assertFalse(user.has_perm("some_permissions"))
        
#     def test_is_staff(self):
#         user = User(email="testemail")
#         self.assertFalse(user.is_staff)

# class SurveyMethodTest(TestCase):
#     def test__str__(self):
#         survey = Survey(s_name="testsurvey")

# class Question_typesMethodTest(TestCase):
#     def test__str__(self):
#        q = Question_types(type="r")