# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-03-15 12:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('annotation_tool', '0057_auto_20170302_1634'),
    ]

    operations = [
        migrations.AlterField(
            model_name='segment',
            name='name',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='wav',
            name='name',
            field=models.CharField(max_length=1000),
        ),
    ]
