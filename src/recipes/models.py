from random import randint

from django.db import models
from django.contrib.auth import get_user_model
from django.db.models import Q

from django_measurement.models import MeasurementField
from measurement.measures import Volume
from model_utils.models import TimeStampedModel

User = get_user_model()


class Recipe(TimeStampedModel):
    title = models.CharField('Title', max_length=255, help_text='Title of the recipe.')
    description = models.TextField('Description', blank=True, null=True)
    owner = models.ForeignKey(User, blank=True, null=True)
    expected_production = MeasurementField(verbose_name='Expected Production', measurement=Volume, blank=True, null=True)

    og = models.DecimalField('OG', max_digits=4, decimal_places=3, blank=True, null=True, help_text='Original Gravity')
    fg = models.DecimalField('FG', max_digits=4, decimal_places=3, blank=True, null=True, help_text='Final Gravity')
    ibu = models.PositiveIntegerField('IBU', blank=True, null=True, help_text='International Bitterness Unit')
    srm = models.PositiveIntegerField('SRV', blank=True, null=True, help_text='Standard Reference Method')
    abv = models.DecimalField('ABV', max_digits=4, decimal_places=2, blank=True, null=True,
                              help_text='Alcohol by Volume')
    steps = models.TextField('Steps')
    observations = models.TextField('Observations', blank=True, null=True)

    def __str__(self):
        return self.title

    @staticmethod
    def get_random():
        recipes = Recipe.objects.filter(owner=None)
        recipes_ids = recipes.values_list('id', flat=True)

        if not len(recipes_ids):
            return None

        index = randint(0, recipes.count() - 1)
        return recipes[index]

    @staticmethod
    def get_suggestion(user):
        from src.ingredients.models import UserIngredient

        user_ingredients = UserIngredient.objects.filter(user=user)
        if not user_ingredients.count():
            return None

        user_ingredients_ids = sorted(list(user_ingredients.values_list('ingredient_type', flat=True)))
        found_recipes = Recipe.objects.filter(Q(owner=None) | Q(owner=user)).filter(ingredients__in=user_ingredients_ids)

        suggestions = []
        for recipe in found_recipes:
            found_ingredients_ids = sorted(list(recipe.ingredients.all().values_list('ingredient_type', flat=True)))

            if len(found_ingredients_ids) > len(user_ingredients_ids):
                continue

            if user_ingredients_ids == found_ingredients_ids:
                suggestions.append(recipe)
                continue

            if not set(found_ingredients_ids).difference(set(user_ingredients_ids)):
                suggestions.append(recipe)
                continue

        if not suggestions:
            return None

        index = randint(0, len(suggestions) - 1)
        return suggestions[index]
