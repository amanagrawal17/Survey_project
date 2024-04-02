from django.urls import path
from surveyapp.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('register', UserRegisterView.as_view(), name='register'),
    path('login', UserLoginView.as_view(), name='login'),
    path('profile', UserProfileView.as_view(), name='profile'),
    path('updateprofile', UserUpdateProfileView.as_view(), name='updateprofile'),
    path('changepassword', UserChangePasswordView.as_view(), name='changepassword'),
    path('resetpasswordemail', ResetPasswordEmailView.as_view(), name='resetpasswordemail'),
    path('resetpassword/<uid>/<token>/', UserPasswordResetView.as_view(), name='resetpassword'),
    path('surveycreate', SurveyCreateView.as_view(), name='surveycreate'),
    path('surveydetail', SurveyDetailView.as_view(), name='surveydetail'),
    path('questiontypesdetail', QuestiontypesDetailView.as_view(), name='questiontypesdetail'),
    path('surveyupdate/<int:pk>', SurveyUpdateView.as_view(), name='surveyupdate'),
    path('surveydelete/<int:pk>', SurveyDeleteView.as_view(), name='surveydelete'),
    # path('questioncreate', QuestionCreateView.as_view(), name='questioncreate'),
    # path('questiondetail', QuestionDetailView.as_view(), name='questiondetail'),
    # path('questionupdate/<int:pk>', QuestionUpdateView.as_view(), name='questionupdate'),
    # path('questiondelete/<int:pk>', QuestionDeleteView.as_view(), name='questiondelete'),
    path('questions', QuestionAPIView.as_view(), name='question-list'),
    path('questions/<int:pk>', QuestionAPIView.as_view(), name='question-detail'),
    
    path('responsescreate', ResponseCreateView.as_view(), name='responsecreate'),
    path('responsesupdate/<int:pk>', ResponseUpdateView.as_view(), name='responseupdate'),
    path('responsesdetail', QuestionDetailView.as_view(), name='responsedetail'),
    path('responses/delete/<int:pk>', ResponseDeleteView.as_view(), name='responsedelete'),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)