from rest_framework.routers import DefaultRouter
from .views import ClientViewSet

router = DefaultRouter()
router.register('client', ClientViewSet)


urlpatterns=router.urls