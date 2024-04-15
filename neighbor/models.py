from django.db import models

from base.models import BaseModel


# Create your models here.
class Neighbor(BaseModel):
    pass

    def __str__(self) -> str:
        return str(self.mac_addr)
