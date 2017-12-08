# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-12-08 00:17
from __future__ import unicode_literals

from django.db import migrations, models
import django_measurement.models


class Migration(migrations.Migration):

    dependencies = [
        ('ingredients', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipeingredient',
            name='quantity',
        ),
        migrations.RemoveField(
            model_name='recipeingredient',
            name='unit',
        ),
        migrations.RemoveField(
            model_name='useringredient',
            name='quantity',
        ),
        migrations.RemoveField(
            model_name='useringredient',
            name='unit',
        ),
        migrations.AddField(
            model_name='recipeingredient',
            name='type',
            field=models.CharField(choices=[('grain', 'Grain'), ('hop', 'Hop'), ('yeast', 'Yeast'), ('water', 'Water'), ('additive', 'Additive')], default=None, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='recipeingredient',
            name='volume_quantity',
            field=django_measurement.models.MeasurementField(blank=True, measurement_class='Volume', null=True),
        ),
        migrations.AddField(
            model_name='recipeingredient',
            name='weight_quantity',
            field=django_measurement.models.MeasurementField(blank=True, measurement_class='Mass', null=True),
        ),
        migrations.AddField(
            model_name='useringredient',
            name='type',
            field=models.CharField(choices=[('grain', 'Grain'), ('hop', 'Hop'), ('yeast', 'Yeast'), ('water', 'Water'), ('additive', 'Additive')], default='grain', max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='useringredient',
            name='volume_quantity',
            field=django_measurement.models.MeasurementField(blank=True, measurement_class='Volume', null=True),
        ),
        migrations.AddField(
            model_name='useringredient',
            name='weight_quantity',
            field=django_measurement.models.MeasurementField(blank=True, measurement_class='Mass', null=True),
        ),
    ]
