from django.urls import path
from surveyapp.views import UserRegisterView, UserLoginView, UserProfileView , UserChangePasswordView, ResetPasswordEmailView , UserPasswordResetView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('changepassword/', UserChangePasswordView.as_view(), name='changepassword'),
    path('resetpasswordemail/', ResetPasswordEmailView.as_view(), name='resetpasswordemail'),
    path('resetpassword/<uid>/<token>/', UserPasswordResetView.as_view(), name='resetpassword'),
]