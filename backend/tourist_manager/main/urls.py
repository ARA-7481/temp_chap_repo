from rest_framework import routers
from .api import VehicleViewSet, TouristLogViewSet, VehicleLogViewSet

router = routers.DefaultRouter()
router.register('api/vehicle', VehicleViewSet, 'vehicle')
router.register('api/touristlog', TouristLogViewSet, 'touristlog')
router.register('api/vehiclelog', VehicleLogViewSet, 'vehiclelog')

urlpatterns = router.urls