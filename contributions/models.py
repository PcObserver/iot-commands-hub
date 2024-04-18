from polymorphic.models import PolymorphicModel
from django.db import models
import uuid

from users.models import User


class Contribution(PolymorphicModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="contributions")
    
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = ("Contribution")
        verbose_name_plural = ("Contributions")