# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-12-08 00:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ingredients', '0002_auto_20171208_0017'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipeingredient',
            old_name='type',
            new_name='ingredient_type',
        ),
        migrations.RenameField(
            model_name='useringredient',
            old_name='type',
            new_name='ingredient_type',
        ),
    ]