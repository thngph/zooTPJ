from django.urls import path
from . import views
from .views import DonateAPI
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('charge/', views.charge, name="charge"),
    path('success/<str:args>/', views.successMsg, name="success"),
    path('api/donate/', DonateAPI.as_view(), name='donate_api_view')
]