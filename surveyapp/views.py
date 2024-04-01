from rest_framework.response import Response
from rest_framework import status, request
from .models import Survey
from rest_framework import generics
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from surveyapp.serializers import *
from surveyapp.renderers import UserRenderer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated

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
            return Response({'token': token, 'msg': 'Registration Successfull'},
                            status=status.HTTP_201_CREATED)
        return Response(serializer.erroes, status=status.HTTP_400_BAD_REQUEST)


class UserLoginView(APIView):
    renderer_classes = [UserRenderer]

    def post(self, request, format=None):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            email = serializer.data.get('email')
            password = serializer.data.get('password')
            user = authenticate(email=email, password=password)
            if user is not None:
                token = get_tokens_for_user(user)
                return Response({'token': token, 'msg': 'Login Successfull'},
                                status=status.HTTP_200_OK)
            else:
                return Response({'errors': {'non_feild_errors': ['Email or Password is not valid']}},
                                status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.erroes, status=status.HTTP_400_BAD_REQUEST)


class UserProfileView(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        serializer = UserProfileSerializer(request.user)

        return Response(serializer.data, status=status.HTTP_200_OK)


class UserUpdateProfileView(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]

    def put(self, request):
        """
        `Update User`
        """
        user = self.request.user
        serializer = UserUpdateProfileSerializer(
            user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserChangePasswordView(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        serializer = UserChangePasswordSerializer(
            data=request.data, context={'user': request.user})
        if serializer.is_valid(raise_exception=True):
            return Response({'msg': 'Password Changed Successfull'},
                            status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ResetPasswordEmailView(APIView):
    renderer_classes = [UserRenderer]

    def post(self, request, format=None):
        serializer = RestPasswordEmailSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            return Response({'msg': 'Password Reset Link send. Please check your Registered Email.'},
                            status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserPasswordResetView(APIView):
    renderer_classes = [UserRenderer]

    def post(self, request, uid, token,  format=None):
        serializer = UserPasswordResetSerializer(
            data=request.data, context={'uid': uid, 'token': token})
        if serializer.is_valid(raise_exception=True):
            return Response({'msg': 'Password Changed Successfull'},
                            status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SurveyCreateView(APIView):
    renderer_classes = [UserRenderer]

    def post(self, request, format=None):
        serializer = SurveyCreateSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            survey = serializer.save()
            # token = get_tokens_for_user(survey)
            return Response({'msg': 'Survey Created Successfull'},
                            status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SurveyDetailView(APIView):
    def get(self, request,  format=None):
        survey = Survey.objects.all()
        serializer = SurveyDetailsSerializer(survey, many=True)
        return Response(serializer.data)


class SurveyUpdateView(generics.UpdateAPIView):
    queryset = Survey.objects.all()
    serializer_class = SurveyUpdateSerializer


class SurveyDeleteView(generics.DestroyAPIView):
    queryset = Survey.objects.all()
    serializer_class = SurveyDetailsSerializer


class QuestiontypesDetailView(APIView):
    def get(self, request,  format=None):
        questiontypes = Question_types.objects.all()
        serializer = QuestiontypesDetailSerializer(questiontypes, many=True)
        return Response(serializer.data)


class QuestionCreateView(APIView):
    renderer_classes = [UserRenderer]

    def post(self, request, format=None):
        serializer = QuestionCreateSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            question = serializer.save()
            # token = get_tokens_for_user(survey)
            return Response({'msg': 'Question Created Successfull'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class QuestionDetailView(APIView):
    def get(self, request,  format=None):
        question = Questions.objects.all()
        serializer = QuestionDetailsSerializer(question, many=True)
        return Response(serializer.data)


class QuestionUpdateView(generics.UpdateAPIView):
    queryset = Questions.objects.all()
    serializer_class = QuestionUpdateSerializer


class QuestionDeleteView(generics.DestroyAPIView):
    queryset = Questions.objects.all()
    serializer_class = QuestionDetailsSerializer
    
    

class ResponseCreateView(generics.CreateAPIView):
    queryset = Responses.objects.all()
    serializer_class = ResponseSerializer

class ResponseUpdateView(generics.UpdateAPIView):
    queryset = Responses.objects.all()
    serializer_class = ResponseSerializer

# class ResponseRetrieveView(generics.RetrieveAPIView):
#     queryset = Responses.objects.all()
#     serializer_class = ResponseSerializer
    
class QuestionDetailView(APIView):
    def get(self, request,  format=None):
        responses = Responses.objects.all()
        serializer = ResponseSerializer(responses, many=True)
        return Response(serializer.data)

class ResponseDeleteView(generics.DestroyAPIView):
    queryset = Responses.objects.all()
    serializer_class = ResponseSerializer