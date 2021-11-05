from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index),
    path('ticket/', views.redirect_ticket, name='ticket')
]