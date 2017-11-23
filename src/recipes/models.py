from django.db import models

from model_utils.models import TimeStampedModel

KILOGRAM = 'kg'
GRAM = 'g'
MILIGRAM = 'mg'
LITRE = 'l'
MILILITRE = 'ml'

UNIT_CHOICES = (
    (MILIGRAM, 'mg'),
    (GRAM, 'gram'),
    (KILOGRAM, 'kilogram'),
    (LITRE, 'litre'),
    (MILILITRE, 'ml'),
)


class Recipe(TimeStampedModel):
    title = models.CharField('Title', max_length=255, help_text='Title of the recipe.')
    og = models.DecimalField('OG', max_digits=4, decimal_places=4, blank=True, null=True, help_text='Original Gravity')
    fg = models.DecimalField('FG', max_digits=4, decimal_places=4, blank=True, null=True, help_text='Final Gravity')
    ibu = models.PositiveIntegerField('IBU', blank=True, null=True, help_text='International Bitterness Unit')
    srm = models.PositiveIntegerField('SRV', blank=True, null=True, help_text='Standard Reference Method')
    abv = models.DecimalField('ABV', max_digits=3, decimal_places=2, blank=True, null=True,
                              help_text='Alcohol by Volume')

    steps = models.TextField('Steps')
    observations = models.TextField('Observations', blank=True, null=True)


class Ingredient(TimeStampedModel):
    name = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField()
    unit = models.CharField(max_length=2, choices=UNIT_CHOICES)
    recipe = models.ForeignKey(Recipe)
