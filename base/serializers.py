from rest_framework.serializers import ModelSerializer
from .models import *



class DeviceModelSerializer(ModelSerializer):
    class Meta:
        model = DeviceModel
        fields = '__all__'