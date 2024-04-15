from rest_framework.routers import DefaultRouter
from .views import NeighborViewSet

router = DefaultRouter()
router.register('neighbor', NeighborViewSet)


urlpatterns=router.urls