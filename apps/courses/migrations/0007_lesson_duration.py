# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-11-23 15:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0006_video_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='duration',
            field=models.IntegerField(default=0, verbose_name='\u89c6\u9891\u65f6\u957f(\u5206)'),
        ),
    ]
