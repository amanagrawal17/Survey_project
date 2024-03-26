from rest_framework import serializers
from surveyapp.models import User

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
        