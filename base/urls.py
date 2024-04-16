from rest_framework.routers import DefaultRouter
from .views import DeviceModelViewSet

router = DefaultRouter()
router.register('base-device', DeviceModelViewSet)


urlpatterns=router.urls