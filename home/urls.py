from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import ProfileAPI, RegisterAPI

urlpatterns = [
    path('', views.index),
    path('register/', views.register, name="register"),
    path('infoUser/', views.infoUser, name="infoUser"),
    path('login/', auth_views.LoginView.as_view(template_name="home/login.html"), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    path('api/profile/', ProfileAPI.as_view(), name='profile_api_view'),
    path('api/register/', RegisterAPI.as_view(), name='register_api_view')
]