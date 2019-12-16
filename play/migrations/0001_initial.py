# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-12-05 19:35
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
                ('title', models.CharField(max_length=30)),
                ('blog_description', models.TextField(max_length=300)),
                ('posted_by', models.CharField(max_length=30)),
                ('bloger', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cat_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_content', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('post_description', models.CharField(max_length=300)),
                ('posted_by', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Fitness_activities',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='images/')),
                ('description', models.CharField(max_length=3000)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='play.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location_name', models.CharField(max_length=30, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_pic', models.ImageField(null=True, upload_to='photos/')),
                ('fullname', models.CharField(max_length=255, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Sector',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sector_name', models.CharField(max_length=30, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('t_name', models.CharField(max_length=400)),
                ('description', models.CharField(max_length=300)),
                ('members', models.IntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12), (13, 13), (14, 14), (15, 15), (16, 16), (17, 17), (18, 18), (19, 19), (20, 20), (21, 21), (22, 22), (23, 23), (24, 24), (25, 25), (26, 26), (27, 27), (28, 28), (29, 29), (30, 30), (31, 31), (32, 32), (33, 33), (34, 34), (35, 35), (36, 36), (37, 37), (38, 38), (39, 39)], default=0)),
                ('ground', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='play.Fitness_activities')),
            ],
        ),
        migrations.AddField(
            model_name='profile',
            name='team',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='play.Team'),
        ),
        migrations.AddField(
            model_name='profile',
            name='username',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='fitness_activities',
            name='sector',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='play.Sector'),
        ),
        migrations.AddField(
            model_name='events',
            name='poster',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='play.Fitness_activities'),
        ),
        migrations.AddField(
            model_name='comment',
            name='poster',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='play.Fitness_activities'),
        ),
        migrations.AddField(
            model_name='comment',
            name='username',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='chat',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='play.Team'),
        ),
        migrations.AddField(
            model_name='chat',
            name='username',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='blog',
            name='poster',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='play.Fitness_activities'),
        ),
        migrations.AddField(
            model_name='blog',
            name='profile',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='play.Profile'),
        ),
    ]
