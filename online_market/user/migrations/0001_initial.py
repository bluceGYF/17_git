# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('is_delete', models.BooleanField(default=False)),
                ('user_name', models.CharField(max_length=50)),
                ('user_pass', models.CharField(max_length=110)),
                ('user_addr', models.CharField(max_length=100)),
                ('user_tele', models.CharField(max_length=11)),
                ('user_code', models.CharField(max_length=6)),
                ('user_true_name', models.CharField(max_length=50)),
                ('user_card_id', models.CharField(max_length=30)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
