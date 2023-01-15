from main.models import Vehicle, TouristLog, VehicleLog
from rest_framework import viewsets, permissions
from .serializers import VehicleSerializer, TouristLogSerializer, VehicleLogSerializer

class VehicleViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = VehicleSerializer

    def perform_create(self, serializer):
        serializer.save(added_by=self.request.user)

class TouristLogViewSet(viewsets.ModelViewSet):
    queryset = TouristLog.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = TouristLogSerializer

    def perform_create(self, serializer):
        serializer.save(added_by=self.request.user)

class VehicleLogViewSet(viewsets.ModelViewSet):
    queryset = VehicleLog.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = VehicleLogSerializer

    def perform_create(self, serializer):
        serializer.save(added_by=self.request.user)
