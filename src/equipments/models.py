from django.db import models
from model_utils.models import TimeStampedModel
from django.contrib.auth import get_user_model

from src.units.models import UNIT_CHOICES

User = get_user_model()


class Equipment(TimeStampedModel):
    """
    AIRLOCK
    BOILING_POT
    BOTTLE
    BOTTLE_CAPPER
    BOOTLE_CAPS
    BOOTLE_BRUSH
    FERMENTER
    MEASURING_CUP
    SIPHON
    RACKING_CANE
    BOTTLE_FILLER
    STIRRING_PADDLE
    THERMOMETER
    BOTTLING_BUCKET
    HYDROMETER
    WINE_THIEF
    HYDROMETER_JAR
    WORT_CHILLER
    STRAINER
    """

    name = models.CharField(unique=True, max_length=255)
    description = models.TextField(blank=True, null=True)


class UserEquipment(TimeStampedModel):
    # TODO: Later on will have a link to batch indicating that is not available.

    user = models.ForeignKey(User)
    equipment = models.ForeignKey(Equipment)
    capacity = models.DecimalField('Qty', max_digits=8, decimal_places=4)
    unit = models.CharField(max_length=2, choices=UNIT_CHOICES)
