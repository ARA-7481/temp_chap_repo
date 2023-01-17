from rest_framework import serializers
from main.models import Vehicle, Tourist, LogDetails

class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = '__all__'

class TouristSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tourist
        fields = '__all__'

class LogDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = LogDetails
        fields = '__all__'