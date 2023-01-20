from rest_framework import serializers
from main.models import Vehicle, Tourist, LogDetails


class LogDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = LogDetails
        fields = '__all__'

class TouristSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tourist
        fields = '__all__'
        #fields = ('id', 'name', 'age', 'gender', 'address', 'contact_number', 'log_info',)
        
class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = '__all__'
