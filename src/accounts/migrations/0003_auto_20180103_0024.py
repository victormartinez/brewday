# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-01-03 00:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_userpreferences'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserPreferences',
            new_name='UserPreference',
        ),
    ]
