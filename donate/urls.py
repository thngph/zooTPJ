from django.urls import path
from . import views
from .views import DonateAPI
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index),
    path('ticket/', views.redirect_ticket, name='ticket'),
    path('api/donate/', DonateAPI.as_view(), name='donate_api_view')
]