from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from surveyapp.serializers import UserRegisterSerializer, UserLoginSerializer

class UserRegisterView(APIView):
    def post(self, request, format=None):
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            return Response({'msg': 'Registration Successfull'},
            status=status.HTTP_201_CREATED)
        return Response(serializer.erroes,status=status.HTTP_400_BAD_REQUEST)
    

class UserLoginView(APIView):
    def post(self, request, format=None):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            email = serializer.data.get('email')
            password = serializer.data.get('password')
            user = authenticate(email=email,password=password)
            if user is not None:
                return Response({'msg': 'Login Successfull'},
            status=status.HTTP_200_OK)
            else :
                return Response({'errors':{'non_feild_errors':['Email or Password is not valid']}},
            status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.erroes,status=status.HTTP_400_BAD_REQUEST)      
                
        