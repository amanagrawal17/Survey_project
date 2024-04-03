from django.test import TestCase
# from .models import User

# print("this is test")
# class UserModelTest(TestCase):
#     def test_create_user(self):
#         print ("inside test create fun")
#         email = "test@example.com"
#         # name = "test user"
#         password = "textpassword"
        
#         user = User.objects.create_user(email=email, name=name, password=password)
#         print("Userr :", user)
#         self.assertEqual(user.email, email)
#         # self.assertEqual(user.name, name)
#         self.assertFalse(user.is_active)
#         self.assertFalse(user.is_admin)
#         self.assertFalse(user.is_staff)
#         self.assertTrue(user.check_password(password))