# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-12 23:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galerija', '0008_auto_20170113_0014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='picture',
            name='image',
            field=models.ImageField(upload_to='galerija/static/photos/%Y/%m/'),
        ),
    ]
