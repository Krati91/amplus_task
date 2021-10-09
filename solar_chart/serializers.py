from rest_framework import serializers
from .models import SolarPlant


class PlantSerializer(serializers.ModelSerializer):
    class Meta:
        model = SolarPlant
        fields = ['plant_id', 'date', 'parameter', 'value']
