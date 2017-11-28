from django.db import models
from django.core.exceptions import FieldError
from django.contrib.auth import get_user_model

from model_utils.models import TimeStampedModel

from src.recipes.models import Recipe
from src.units.models import UNIT_CHOICES

User = get_user_model()


class Ingredient(TimeStampedModel):
    # To DO: change quantity to decimal field
    name = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField('Qty')
    unit = models.CharField(max_length=2, choices=UNIT_CHOICES)

    class Meta:
        abstract = True


class RecipeIngredient(Ingredient):
    recipe = models.ForeignKey(Recipe)


class UserIngredient(Ingredient):
    user = models.ForeignKey(User)

    def can_decrease_by(self, amount):
        return self.quantity >= amount

    def increase(self, amount):
        self.quantity += amount

    def decrease(self, amount):
        if not self.can_decrease_by(amount):
            raise FieldError('The current quantity corresponds to less than the amount decreased.')

        self.quantity -= amount