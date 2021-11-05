from django.urls import path, include
import donate
from . import views
from donate import urls
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index),
    path('donate/', views.redirect_donate, name='donate')
]
