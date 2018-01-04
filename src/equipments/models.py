from django.db import models
from django.contrib.auth import get_user_model

from django_measurement.models import MeasurementField
from measurement.measures import Volume
from model_utils.models import TimeStampedModel

User = get_user_model()


class Equipment(TimeStampedModel):
    name = models.CharField(unique=True, max_length=255)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True, null=True)
    is_measured = models.BooleanField()

    def __str__(self):
        return self.name


class UserEquipment(TimeStampedModel):
    # TODO: Later on will have a link to batch indicating that is not available.
    # TODO: Insight: tem equipamentos que funcionam como gargalo. Tipo, adianta fazer tudo e não ter garrafa?? Order de prioridades

    user = models.ForeignKey(User)
    equipment = models.ForeignKey(Equipment)
    quantity = models.PositiveIntegerField('Qty')
    volume_capacity = MeasurementField(measurement=Volume, blank=True, null=True)
