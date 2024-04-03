from django.test import TestCase
from .models import User

class UserModelTest(TestCase):
    def test_create_superuser(self):
        # print ("inside test create fun")
        email = "test@example.com"
        first_name = "test "
        last_name = "user"
        password = "textpassword"
        
        user = User.objects.create_user(email=email, first_name=first_name, last_name=last_name, password=password, created_at=None, updated_at=None)
        # print("Userr :", user)
        self.assertEqual(user.email, email)
        self.assertEqual(user.first_name, first_name)
        self.assertEqual(user.last_name, last_name)
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_admin)
        self.assertFalse(user.is_staff)
        self.assertTrue(user.check_password(password))
        print("test case run successfuly")

