# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-22 17:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='status',
            field=models.CharField(choices=[('open', 'open'), ('cancelled', 'cancelled'), ('submitted', 'submitted'), ('processed', 'processed'), ('delivered', 'delivered')], max_length=255),
        ),
    ]
