from .models import Animal
from rest_framework import serializers


class AnimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Animal
        fields = (
            'animal_ID', 'animal_name', 'description', 'img', 'profile_img'
        )
