from rest_framework.serializers import ModelSerializer
from .models import *



class VIFSerializer(ModelSerializer):
    class Meta:
        model = VIF
        fields = '__all__'