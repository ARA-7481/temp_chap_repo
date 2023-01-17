from rest_framework import routers
from .api import VehicleViewSet, TouristViewSet, LogDetailsViewSet

router = routers.DefaultRouter()
router.register('api/vehicle', VehicleViewSet, 'vehicle')
router.register('api/tourist', TouristViewSet, 'tourist')
router.register('api/logdetails', LogDetailsViewSet, 'logdetails')

urlpatterns = router.urls