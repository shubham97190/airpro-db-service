from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny

from client.models import Client
from client.serializers import ClientSerializer

# Create your views here.
class ClientViewSet(ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    http_method_names = ['get','post','update','delete']
    permission_classes = [AllowAny]