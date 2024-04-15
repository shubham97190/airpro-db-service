from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny

from vif.models import VIF
from vif.serializers import VIFSerializer


# Create your views here.
class VIFViewSet(ModelViewSet):
    queryset = VIF.objects.all()
    serializer_class = VIFSerializer
    http_method_names = ['get', 'post', 'update', 'delete']
    permission_classes = [AllowAny]
