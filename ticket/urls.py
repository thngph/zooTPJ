from django.urls import path, include
import donate
from . import views
from .views import TicketAPI
from donate import urls
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index),
    path('charge/', views.charge, name="charge"),
    path('success/', views.successMsg, name="success"),
    path('api/ticket/', TicketAPI.as_view(), name='ticket_api_view')
]
