# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2019-05-17 11:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('queryMenu', '0005_auto_20190514_1450'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='status',
            field=models.CharField(default='启用', max_length=30, verbose_name='是否启用'),
        ),
    ]