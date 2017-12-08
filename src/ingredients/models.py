from django.db import models
from django.contrib.auth import get_user_model

from django_measurement.models import MeasurementField
from model_utils.models import TimeStampedModel
from measurement.measures import Volume, Weight

from src.recipes.models import Recipe

User = get_user_model()


class Ingredient(TimeStampedModel):
    GRAIN = 'grain'
    HOP = 'hop'
    YEAST = 'yeast'
    WATER = 'water'
    ADDITIVE = 'additive'
    INGREDIENT_TYPE_CHOICES = (
        (GRAIN, 'Grain'),
        (HOP, 'Hop'),
        (YEAST, 'Yeast'),
        (WATER, 'Water'),
        (ADDITIVE, 'Additive'),
    )

    name = models.CharField(max_length=255)
    ingredient_type = models.CharField(choices=INGREDIENT_TYPE_CHOICES, max_length=10)
    volume_quantity = MeasurementField(measurement=Volume, blank=True, null=True)
    weight_quantity = MeasurementField(measurement=Weight, blank=True, null=True)

    class Meta:
        abstract = True


class RecipeIngredient(Ingredient):
    recipe = models.ForeignKey(Recipe)

    def __str__(self):
        if self.volume_quantity:
            return "{}: {}".format(self.name, self.volume_quantity)
        return "{}: {}".format(self.name, self.weight_quantity)


class UserIngredient(Ingredient):
    user = models.ForeignKey(User)
