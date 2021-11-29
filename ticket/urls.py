from django.urls import path, include
import donate
from . import views
from .views import TicketAPI
from donate import urls
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index),
    path('charge/', views.charge, name="ticket_charge"),
    path('success/<str:args>/', views.successMsg, name="ticket_success"),
    path('api/ticket/', TicketAPI.as_view(), name='ticket_api_view')
]
