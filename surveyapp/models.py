from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


#Custom User Manager
class UserManager(BaseUserManager):

    def create_user(self, email, password, first_name, last_name):
                    # , created_at, updated_at):
        if not email:
            raise ValueError("Email must be provided")
        if not password:
            raise ValueError("Password is not provided")

        user = self.model(
            email = self.normalize_email(email),
            first_name = first_name,
            last_name = last_name,
            # created_at = created_at,
            # updated_at = updated_at,
            
            

        )
        
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, first_name, last_name, password=None ):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            password=password,
            first_name= first_name,
            last_name= last_name,
            
            
            
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

# Custom User Model
class User(AbstractBaseUser):
    email = models.EmailField(verbose_name='Email', unique=True, max_length=255)
    first_name = models.CharField(max_length=240, null=True, blank=True)
    last_name = models.CharField(max_length=240, null=True, blank=True)
    password = models.CharField(max_length=240)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    picture = models.ImageField(upload_to="User_profile", blank=True)
    is_staff = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    
    objects = UserManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name','last_name']
    
    def __str__(self):
        return self.email
    
    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return self.is_admin

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
        
     
class Survey(models.Model):     
    s_name = models.CharField(max_length=240, null=False, blank=False)
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)
    

class Question_types(models.Model):
    TYPES = (
    ('radio', 'Radio'),
    ('checkbox', 'Checkbox'),
    ('text', 'Text'),
    ('multiple_choice', 'Multiple Choice'),
    ('rating_scale', 'Rating Scale')
    )
    type = models.CharField(max_length=20, choices=TYPES)

    def __str__(self):
        return self.type

class Questions(models.Model):
    
    heading = models.CharField(max_length=255)
    type = models.ForeignKey(Question_types, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    options = models.JSONField()

    def __str__(self):
        return self.heading
    

class Responses(models.Model):
    question_id = models.ForeignKey(Questions, on_delete=models.CASCADE)
    response_data = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # def __str__(self):
    #     return f"Response to {self.question.text}"