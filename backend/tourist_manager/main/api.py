from main.models import Vehicle, Tourist, LogDetails
from rest_framework import viewsets, permissions
from .serializers import VehicleSerializer, TouristSerializer, LogDetailsSerializer

class VehicleViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = VehicleSerializer

    def perform_create(self, serializer):
        serializer.save(added_by=self.request.user)

class TouristViewSet(viewsets.ModelViewSet):
    queryset = Tourist.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = TouristSerializer

    def perform_create(self, serializer):
        serializer.save(added_by=self.request.user)

class LogDetailsViewSet(viewsets.ModelViewSet):
    queryset = LogDetails.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = LogDetailsSerializer

    def perform_create(self, serializer):
        serializer.save(added_by=self.request.user)
