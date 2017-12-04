from django.db import models
from model_utils.models import TimeStampedModel
from django.contrib.auth import get_user_model

from src.recipes.models import Recipe
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

    def __str__(self):
        return self.name


class UserEquipment(TimeStampedModel):
    # TODO: Later on will have a link to batch indicating that is not available.
    # TODO: Insight: tem equipamentos que funcionam como gargalo. Tipo, adianta fazer tudo e não ter garrafa?? Order de prioridades

    user = models.ForeignKey(User)
    equipment = models.ForeignKey(Equipment)
    quantity = models.PositiveIntegerField('Qty')
    capacity = models.DecimalField('Capacity', max_digits=8, decimal_places=4)
    unit = models.CharField(max_length=2, choices=UNIT_CHOICES)


class RecipeEquipment(TimeStampedModel):
    recipe = models.ForeignKey(Recipe)
    equipment = models.ForeignKey(Equipment)
    quantity = models.PositiveIntegerField('Qty')
    capacity = models.DecimalField('Capacity', max_digits=8, decimal_places=4)
    unit = models.CharField(max_length=2, choices=UNIT_CHOICES)
