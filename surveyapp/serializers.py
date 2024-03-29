from xml.dom import ValidationErr
from rest_framework import serializers
from surveyapp.models import User,Survey
from django.utils.encoding import smart_str, force_bytes, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from surveyapp.utils import Util
import pathlib


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'password', 'first_name', 'last_name']
        extra_kwargs={
            'password':{'write_only':True}
        }
        
    def validate(self, attrs):
        password = attrs.get('password')
        # password2 = attrs.get('password2')
        # if password != password2:
        #     raise serializer.ValidationError("Password and Confirm Password doesn't match")
        # return super().validate(attrs)
        return attrs
    
    def create(self, validate_data):
        return User.objects.create_user(**validate_data)
    


class UserLoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255)
    class Meta:
        model = User
        fields = ['email','password']
        
        
class UserProfileSerializer(serializers.ModelSerializer):
    # picture_url = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'picture']


class UserUpdateProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ( 'first_name', 'last_name','picture')
            
        
class UserChangePasswordSerializer(serializers.Serializer):
    password = serializers.CharField(max_length=255, style={'input_type':'password'}, write_only=True)
    # password2 = serializers.CharField(max_length=255, style={'input_type':'password'}, write_only=True)
    class Meta:
        fields = ['password']
        
    def validate(self, attrs):
        password = attrs.get('password')
        user = self.context.get('user')
        # password2 = attrs.get('password2')
        # if password != password2:
        #     raise serializer.ValidationError("Password and Confirm Password doesn't match")
        user.set_password(password)
        user.save()
        return attrs
    
    
class RestPasswordEmailSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=255)
    class Meta :
        fields = ['email']
        
    def validate(self, attrs):
        email = attrs.get('email')
        if User.objects.filter(email=email).exists():
            user = User.objects.get(email=email)
            uid = urlsafe_base64_encode(force_bytes(user.email))
            print('Encoded UID', uid)
            token = PasswordResetTokenGenerator().make_token(user)
            print('Password Reset Token', token)
            link = 'http://localhost:8000/app/resetpassword/'+uid+'/'+token
            print('Password reset link ',link)
            body = 'Click Following Link to Reset Your password : ' +link
            data = {
                'subject' : 'Reset your Password',
                'body': body,
                'to_email': user.email
            }
            Util.send_email(data)
            return attrs
        else:
            raise validationErr('You are not a registered User')
        

class UserPasswordResetSerializer(serializers.Serializer):
    password = serializers.CharField(max_length=255, style={'input_type':'password'}, write_only=True)
    password2 = serializers.CharField(max_length=255, style={'input_type':'password'}, write_only=True)
    class Meta:
        fields = ['password','password2']
        
    def validate(self, attrs):
        try:
            password = attrs.get('password')
            password2 = attrs.get('password2')
            uid = self.context.get('uid')
            token = self.context.get('token')
            if password != password2:
                raise serializer.ValidationError("Password and Confirm Password doesn't match")
            id = smart_str(urlsafe_base64_decode(uid))
            user = User.objects.get(email=id)
            if not PasswordResetTokenGenerator().check_token(user, token):
                raise ValidationError('Token is not Valid or Expired')      
            user.set_password(password)
            user.save()
            return attrs
            
        except  DjangoUnicodeDecodeError as identifier:
            PasswordResetTokenGenerator().check_token(user, token)
            raise ValidationError('Token is not Valid or Expired')  
        
        
class SurveyCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Survey
        fields = ['s_id', 's_name']
        def validate(self, attrs):
            s_id = attrs.get('s_id')
            s_name = attrs.get('s_name')
            return attrs
        
        def create(self, validate_data):
            return Survey.objects.create_survey(**validate_data)
        

class SurveyDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Survey
        fields = ['s_id', 's_name']

class SurveyUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Survey
        fields = ['s_name'] 