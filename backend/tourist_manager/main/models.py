from django.db import models
from django.contrib.auth.models import User


class Vehicle(models.Model):
    plate_number = models.CharField(max_length=20, unique=True)
    #driver_name = models.CharField(max_length=100) latest driver?
    private = models.BooleanField(default=False)
    num_passengers = models.PositiveIntegerField()
    description = models.TextField()
    #vehicle_contactnumber = models.CharField(blank=True, max_length=20, null=True)
    visit_count = models.PositiveIntegerField()

class TouristLog(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.SET_NULL, blank=True, null=True)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    contact_number = models.CharField(max_length=20)
    date_time = models.DateTimeField(auto_now_add=True)
    added_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

class VehicleLog(models.Model):
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.SET_NULL, null=True)
    added_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)