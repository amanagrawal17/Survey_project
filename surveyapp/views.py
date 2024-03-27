from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from surveyapp.serializers import UserRegisterSerializer, UserLoginSerializer , USerProfileSerializer
from surveyapp.renderers import UserRenderer
from rest_framework_simplejwt.tokens import RefreshToken

'''Generate Token Manually'''
def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

class UserRegisterView(APIView):
    renderer_classes = [UserRenderer]
    def post(self, request, format=None):
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            token = get_tokens_for_user(user)
            return Response({'token':token,'msg': 'Registration Successfull'},
            status=status.HTTP_201_CREATED)
        return Response(serializer.erroes,status=status.HTTP_400_BAD_REQUEST)
    

class UserLoginView(APIView):
    renderer_classes = [UserRenderer]
    def post(self, request, format=None):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            email = serializer.data.get('email')
            password = serializer.data.get('password')
            user = authenticate(email=email,password=password)
            if user is not None:
                token = get_tokens_for_user(user)
                return Response({'token':token,'msg': 'Login Successfull'},
            status=status.HTTP_200_OK)
            else :
                return Response({'errors':{'non_feild_errors':['Email or Password is not valid']}},
            status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.erroes,status=status.HTTP_400_BAD_REQUEST)      
                
    
class USerProfileView(APIView):
    renderer_classes = [UserRenderer]
    def get(self,request,format=None):
        serializer = USerProfileSerializer(request.user)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_200_OK)