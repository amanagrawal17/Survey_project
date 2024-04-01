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
    path('questioncreate', QuestionCreateView.as_view(), name='questioncreate'),
    path('questiondetail', QuestionDetailView.as_view(), name='questiondetail'),
    path('questionupdate/<int:pk>', QuestionUpdateView.as_view(), name='questionupdate'),
    path('questiondelete/<int:pk>', QuestionDeleteView.as_view(), name='questiondelete'),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)