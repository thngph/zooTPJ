from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import ProfileAPI, RegisterAPI

urlpatterns = [
    path('', views.index, name='home'),
    path('register/', views.register, name="register"),
    path('user/', views.user_info, name="user"),
    path('user/edit', views.edit_user, name="edit_info"),
    path('user/change-pwd', views.change_password, name="pwd"),
    path('user/upload', views.upload, name="upload"),
    path('login/', views.login_view, name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    path('api/profile/', ProfileAPI.as_view(), name='profile_api_view'),
    path('api/register/', RegisterAPI.as_view(), name='register_api_view')
]