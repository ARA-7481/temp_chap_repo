from django.contrib import admin

from .models import Vehicle, TouristLog, VehicleLog

admin.site.register(Vehicle)
admin.site.register(TouristLog)
admin.site.register(VehicleLog)
