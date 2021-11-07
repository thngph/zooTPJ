from rest_framework import serializers
from .models import Ticket
from django.contrib.auth.models import User


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = (
            ' ticketID', 'date_purchased', 'ticket_type', 'price', 'user_ID'
        )
