from django.urls import path
from .import views


urlpatterns = [
    path('register', views.RegisterAPIView.as_view()),
    path('login', views.LoginAPIView.as_view()),
    path('user', views.UserAPIView.as_view()),
    path('refresh', views.RefreshTokenAPIView.as_view()),
    path('logout', views.LogoutAPIView.as_view()),
]
