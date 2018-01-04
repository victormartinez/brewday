from django.db import models
from django.contrib.auth import get_user_model

from django_measurement.models import MeasurementField
from model_utils.models import TimeStampedModel
from measurement.measures import Volume, Weight

from src.recipes.models import Recipe

User = get_user_model()


class IngredientType(TimeStampedModel):
    MEASURED_BY_VOLUME = 'volume'
    MEASURED_BY_WEIGHT = 'weight'
    MEASURED_BY_CHOICES = (
        (MEASURED_BY_VOLUME, 'volume'),
        (MEASURED_BY_WEIGHT, 'weight'),
    )

    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(unique=True)
    measured_by = models.CharField(choices=MEASURED_BY_CHOICES, max_length=10, null=True, blank=True)

    def __str__(self):
        return self.name


class Ingredient(TimeStampedModel):
    name = models.CharField(max_length=255)
    ingredient_type = models.ForeignKey(IngredientType)
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
