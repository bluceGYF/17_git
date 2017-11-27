# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20171106_2325'),
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('is_delete', models.BooleanField(default=False)),
                ('order_number', models.CharField(max_length=50)),
                ('order_status', models.SmallIntegerField(choices=[(1, '待付款'), (2, '代发货'), (3, '待收货'), (4, '已完成')], default=1)),
                ('order_recv', models.CharField(max_length=20)),
                ('order_addr', models.CharField(max_length=50)),
                ('order_tele', models.CharField(max_length=11)),
                ('order_pay', models.SmallIntegerField(choices=[(1, '网银支付'), (2, '信用卡支付'), (3, '财付通支付'), (4, '支付宝支付')], default=1)),
                ('order_user', models.ForeignKey(to='user.User')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Order_GoodsDetails',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('is_delete', models.BooleanField(default=False)),
                ('goods_name', models.CharField(max_length=50)),
                ('goods_price', models.IntegerField()),
                ('goods_image', models.ImageField(upload_to='')),
                ('goods_num', models.IntegerField()),
                ('goods_unit', models.CharField(max_length=10)),
                ('goods_order', models.ForeignKey(to='cart.Order')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
