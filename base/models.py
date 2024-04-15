import uuid
from django.db import models

# Create your models here.
class BaseModel(models.Model):
    id              = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    device_id       = models.CharField(max_length=255, blank=True, null=True)  
    serial_num      = models.CharField(max_length=255, blank=True, null=True)  
    mac_addr        = models.CharField(max_length=255, blank=True, null=True)
    data            = models.JSONField()
    created_on      = models.DateTimeField(auto_now_add=True)
    updated_on      = models.DateTimeField(auto_now=True)

    class Meta:
        abstract=True