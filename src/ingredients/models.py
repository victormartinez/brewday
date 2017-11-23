from django.db import models
from django.contrib.auth import get_user_model

from model_utils.models import TimeStampedModel

from src.recipes.models import Recipe
from src.units.models import UNIT_CHOICES

User = get_user_model()


class Ingredient(TimeStampedModel):
    name = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField()
    unit = models.CharField(max_length=2, choices=UNIT_CHOICES)

    class Meta:
        abstract = True


class RecipeIngredient(Ingredient):
    recipe = models.ForeignKey(Recipe)


class UserIngredient(Ingredient):
    user = models.ForeignKey(User)
