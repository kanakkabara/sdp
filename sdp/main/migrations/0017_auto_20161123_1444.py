# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-23 14:44
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_auto_20161120_1648'),
    ]

    operations = [
        migrations.RenameField(
            model_name='participant',
            old_name='most_recent_unlocked',
            new_name='access',
        ),
    ]
