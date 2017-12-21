from django.db import models
from django.contrib.auth import get_user_model

from django_measurement.models import MeasurementField
from measurement.measures import Volume
from model_utils.models import TimeStampedModel

User = get_user_model()


class Recipe(TimeStampedModel):
    title = models.CharField('Title', max_length=255, help_text='Title of the recipe.')
    description = models.TextField('Description', blank=True, null=True)
    owner = models.ForeignKey(User)
    expected_production = MeasurementField(verbose_name='Expected Production', measurement=Volume, blank=True, null=True)

    og = models.DecimalField('OG', max_digits=4, decimal_places=3, blank=True, null=True, help_text='Original Gravity')
    fg = models.DecimalField('FG', max_digits=4, decimal_places=3, blank=True, null=True, help_text='Final Gravity')
    ibu = models.PositiveIntegerField('IBU', blank=True, null=True, help_text='International Bitterness Unit')
    srm = models.PositiveIntegerField('SRV', blank=True, null=True, help_text='Standard Reference Method')
    abv = models.DecimalField('ABV', max_digits=4, decimal_places=2, blank=True, null=True,
                              help_text='Alcohol by Volume')
    steps = models.TextField('Steps')
    observations = models.TextField('Observations', blank=True, null=True)
