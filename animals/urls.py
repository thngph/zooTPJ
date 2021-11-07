from django.urls import path
from . import views
from .views import AnimalAPI
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index),
    path('api/animals/', AnimalAPI.as_view(), name='animal_api_view')
]