from main.models import Vehicle, Tourist, LogDetails
from rest_framework import viewsets, generics, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import VehicleSerializer, TouristSerializer, LogDetailsSerializer
from rest_framework import filters

class VehicleViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = VehicleSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['plate_number', 'vehicle_classification', 'drivers__name', 'vehicle_type', 'passengers__name', 'description', 'added_by__username']
    ordering_fields = '__all__'
    def perform_create(self, serializer):
        serializer.save(added_by=self.request.user)


class TouristViewSet(viewsets.ModelViewSet):
    queryset = Tourist.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = TouristSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = '__all__'
    ordering_fields = '__all__'
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

