from rest_framework.routers import DefaultRouter
from .views import VIFViewSet

router = DefaultRouter()
router.register('vif', VIFViewSet)

urlpatterns = router.urls
