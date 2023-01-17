from rest_framework import serializers
from main.models import Vehicle, Tourist, LogDetails

class TouristSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tourist
        fields = '__all__'

class LogDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = LogDetails
        fields = '__all__'

class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = '__all__'
