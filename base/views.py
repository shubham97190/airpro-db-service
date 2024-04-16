from rest_framework import status
from rest_framework.response import Response
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
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.data
        obj = DeviceModel.objects.filter(**data)
        if obj.exists():            
            serializer = self.get_serializer(obj[0])
        else:
            self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)