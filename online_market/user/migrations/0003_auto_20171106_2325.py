# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20171106_2122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_tele',
            field=models.CharField(max_length=20),
        ),
    ]
