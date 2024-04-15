from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny

from device.models import Device
from device.serializers import DeviceSerializer

# Create your views here.
class DeviceViewSet(ModelViewSet):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
    http_method_names = ['get','post','update','delete']
    permission_classes = [AllowAny]