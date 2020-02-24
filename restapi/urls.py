from rest_framework import routers

from .views import *

router = routers.DefaultRouter()
router.register(r'mill', MillViewSet)
router.register(r'farmer', FarmerViewSet)
router.register(r'ownermill', OwnermillViewSet)
router.register(r'queue', QueueViewSet)
router.register(r'price', PriceViewSet)
