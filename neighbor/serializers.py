from rest_framework.serializers import ModelSerializer
from .models import *



class NeighborSerializer(ModelSerializer):
    class Meta:
        model = Neighbor
        fields = '__all__'