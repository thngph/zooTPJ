from rest_framework import serializers
from .models import Donate


class DonateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Donate
        fields = ('donation_ID', 'date_donated', 'amount', ' user_ID')