# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-12-02 13:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('play', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
                ('title', models.CharField(max_length=30)),
                ('blog_description', models.CharField(max_length=300)),
                ('posted_by', models.CharField(max_length=30)),
                ('poster', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='play.Fitness_activities')),
            ],
        ),
    ]
