# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-11-21 12:43
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('play', '0003_events'),
    ]

    operations = [
        migrations.RenameField(
            model_name='events',
            old_name='description',
            new_name='post_description',
        ),
        migrations.RenameField(
            model_name='events',
            old_name='event_name',
            new_name='title',
        ),
    ]