# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-20 16:19
from __future__ import unicode_literals

from django.db import migrations, models
import main.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_auto_20161120_1618'),
    ]

    operations = [
        migrations.AlterField(
            model_name='component',
            name='file',
            field=models.FileField(default=None, upload_to=main.models.fileUploadPath),
            preserve_default=False,
        ),
    ]
