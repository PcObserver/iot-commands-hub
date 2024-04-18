from polymorphic.models import PolymorphicModel
from django.db import models
import uuid

from users.models import User


class Contribution(PolymorphicModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="contributions")
    
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = ("Contribution")
        verbose_name_plural = ("Contributions")


class ContributionReview(models.Model):
    class ReviewType(models.IntegerChoices):
        POSITIVE = 0, ('Positive')
        NEGATIVE = 1, ('Negative')
        NONE = 2, ('None')

    contribution = models.ForeignKey(Contribution, on_delete=models.CASCADE, related_name="reviews", null=True)
    reviewer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reviews", null=True)
    type = models.IntegerField(choices=ReviewType.choices, null=False, default=ReviewType.NONE)

    class Meta:
        verbose_name = "Contribution Review"
        verbose_name_plural = ("Contribution Reviews")

    def __str__(self):
        return self.name
