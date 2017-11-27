# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '__first__'),
        ('user', '0003_auto_20171106_2325'),
    ]

    operations = [
        migrations.CreateModel(
            name='GoodsCart',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('is_delete', models.BooleanField(default=False)),
                ('cart_amount', models.IntegerField()),
                ('cart_goods', models.ForeignKey(to='goods.GoodsInfo')),
                ('cart_user', models.ForeignKey(to='user.User')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
