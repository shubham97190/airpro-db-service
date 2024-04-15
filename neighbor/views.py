from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny

from neighbor.models import Neighbor
from neighbor.serializers import NeighborSerializer

# Create your views here.
class NeighborViewSet(ModelViewSet):
    queryset = Neighbor.objects.all()
    serializer_class = NeighborSerializer
    http_method_names = ['get','post','update','delete']
    permission_classes = [AllowAny]