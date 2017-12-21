# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-12-21 00:54
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import django_measurement.models
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('title', models.CharField(help_text='Title of the recipe.', max_length=255, verbose_name='Title')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('expected_production', django_measurement.models.MeasurementField(blank=True, measurement_class='Volume', null=True, verbose_name='Expected Production')),
                ('og', models.DecimalField(blank=True, decimal_places=3, help_text='Original Gravity', max_digits=4, null=True, verbose_name='OG')),
                ('fg', models.DecimalField(blank=True, decimal_places=3, help_text='Final Gravity', max_digits=4, null=True, verbose_name='FG')),
                ('ibu', models.PositiveIntegerField(blank=True, help_text='International Bitterness Unit', null=True, verbose_name='IBU')),
                ('srm', models.PositiveIntegerField(blank=True, help_text='Standard Reference Method', null=True, verbose_name='SRV')),
                ('abv', models.DecimalField(blank=True, decimal_places=2, help_text='Alcohol by Volume', max_digits=4, null=True, verbose_name='ABV')),
                ('steps', models.TextField(verbose_name='Steps')),
                ('observations', models.TextField(blank=True, null=True, verbose_name='Observations')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
