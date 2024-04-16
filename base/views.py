from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny

from .models import DeviceModel
from .serializers import DeviceModelSerializer

# Create your views here.

class DeviceModelViewSet(ModelViewSet):
    queryset = DeviceModel.objects.all()
    serializer_class = DeviceModelSerializer
    http_method_names = ['get','post','update','delete']
    permission_classes = [AllowAny]