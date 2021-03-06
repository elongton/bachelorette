# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-05-06 02:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('place_id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('next_id', models.PositiveIntegerField(default=0)),
                ('instructions', models.TextField(default='')),
                ('plank_clue', models.TextField(default='')),
                ('plank_prompt', models.TextField(default='')),
                ('name_of_establishment', models.CharField(max_length=100)),
                ('plank_answer', models.CharField(max_length=100)),
                ('is_current', models.BooleanField(default=False)),
                ('location_complete', models.BooleanField(default=False)),
            ],
        ),
    ]
