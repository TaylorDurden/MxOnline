# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-11-14 14:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0004_auto_20171112_2342'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='org',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organization.CourseOrg', verbose_name='\u6240\u5728\u673a\u6784'),
        ),
    ]
