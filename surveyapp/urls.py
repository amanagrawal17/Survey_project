from django.urls import path
from surveyapp.views import( UserRegisterView, UserLoginView, 
UserProfileView , UserChangePasswordView, ResetPasswordEmailView , UserPasswordResetView , UserUpdateProfileView,SurveyCreateView,SurveyDetailView
,SurveyUpdateView,SurveyDeleteView)
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('updateprofile/', UserUpdateProfileView.as_view(), name='updateprofile'),
    path('changepassword/', UserChangePasswordView.as_view(), name='changepassword'),
    path('resetpasswordemail/', ResetPasswordEmailView.as_view(), name='resetpasswordemail'),
    path('resetpassword/<uid>/<token>/', UserPasswordResetView.as_view(), name='resetpassword'),
    path('surveycreate/', SurveyCreateView.as_view(), name='surveycreate'),
    path('surveyupdate/<int:pk>/', SurveyUpdateView.as_view(), name='surveyupdate'),
    path('surveydelete/<int:pk>/', SurveyDeleteView.as_view(), name='surveydelete'),
    path('surveydetail/', SurveyDetailView.as_view(), name='surveydetail'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)