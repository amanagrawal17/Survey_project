from django.urls import path
from surveyapp.views import UserRegisterView, UserLoginView , USerProfileView

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('profile/', USerProfileView.as_view(), name='profile'),
]