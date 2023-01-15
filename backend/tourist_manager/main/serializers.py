from rest_framework import serializers
from main.models import Vehicle, TouristLog, VehicleLog

class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = '__all__'

class TouristLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = TouristLog
        fields = '__all__'

class VehicleLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleLog
        fields = '__all__'