# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CityInfo',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('city_name', models.CharField(max_length=50)),
                ('city_code', models.CharField(max_length=50)),
                ('city_baba', models.CharField(max_length=50, blank=True, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='user_cellphone',
            field=models.CharField(max_length=11, default=''),
        ),
    ]
