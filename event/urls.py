from django.urls import path
from . import views
from .views import post_main
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('post/', views.post_main, name='post'),
]
