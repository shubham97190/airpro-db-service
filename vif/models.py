from django.db import models
from base.models import BaseModel

# Create your models here.
class VIF(BaseModel):
    pass

    def __str__(self) -> str:
        return str(self.mac_addr)