from django.test import TestCase
from .models import *

class UserModelTest(TestCase):
    def test_create_superuser(self):
        # print ("inside test create fun")
        email = "amanagrawal1782@gmail.com"
        first_name = "Aman "
        last_name = "Agrawal"
        password = "asdf@123"
        
        superuser = User.objects.create_user(email=email, first_name=first_name, last_name=last_name, password=password, created_at=None, updated_at=None)
        # print("Userr :", user)
        self.assertEqual(superuser.email, email)
        self.assertEqual(superuser.first_name, first_name)
        self.assertEqual(superuser.last_name, last_name)
        self.assertTrue(superuser.is_active)
        self.assertFalse(superuser.is_admin)
        self.assertFalse(superuser.is_staff)
        self.assertTrue(superuser.check_password(password))
        print("test case run successfuly")

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