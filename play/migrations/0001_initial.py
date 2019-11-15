# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-11-13 13:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cat_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Playground',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='images/')),
                ('description', models.CharField(max_length=3000)),
                ('location', models.CharField(max_length=255)),
                ('post_date', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='play.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('t_name', models.CharField(max_length=300)),
                ('description', models.CharField(max_length=300)),
                ('members', models.IntegerField()),
                ('Playground', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='play.Playground')),
            ],
        ),
    ]