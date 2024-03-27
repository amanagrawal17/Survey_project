from xml.dom import ValidationErr
from rest_framework import serializers
from surveyapp.models import User
from django.utils.encoding import smart_str, force_bytes, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode

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
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name']
        
class UserChangePasswordSerializer(serializers.Serializer):
    password = serializers.CharField(max_length=255, style={'input_type':'password'}, write_only=True)
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
    emsil = serializers.EmailField(max_length=255)
    class Meta :
        fields = ['email']
        
    def validate(self, attrs):
        email = attrs.get('email')
        if User.objects.filter(email=email).exists():
            user = User.objects.get(email=email)
        else:
            raise validationErr('You are not a registered User')