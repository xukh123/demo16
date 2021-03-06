# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-09-17 08:39
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Banner',
        ),
        migrations.DeleteModel(
            name='Navigation',
        ),
        migrations.RemoveField(
            model_name='order',
            name='uid',
        ),
        migrations.RemoveField(
            model_name='property',
            name='cate',
        ),
        migrations.DeleteModel(
            name='PropertyValue',
        ),
        migrations.RemoveField(
            model_name='review',
            name='shop',
        ),
        migrations.RemoveField(
            model_name='review',
            name='uid',
        ),
        migrations.RemoveField(
            model_name='shop',
            name='cate',
        ),
        migrations.RemoveField(
            model_name='shopcar',
            name='shop',
        ),
        migrations.RemoveField(
            model_name='shopcar',
            name='uid',
        ),
        migrations.RemoveField(
            model_name='shopimage',
            name='shop',
        ),
        migrations.RemoveField(
            model_name='submenu',
            name='cate',
        ),
        migrations.RemoveField(
            model_name='submenu2',
            name='sub_menu',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='user',
        ),
        migrations.DeleteModel(
            name='AuthUser',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
        migrations.DeleteModel(
            name='Property',
        ),
        migrations.DeleteModel(
            name='Review',
        ),
        migrations.DeleteModel(
            name='Shop',
        ),
        migrations.DeleteModel(
            name='ShopCar',
        ),
        migrations.DeleteModel(
            name='ShopImage',
        ),
        migrations.DeleteModel(
            name='SubMenu',
        ),
        migrations.DeleteModel(
            name='SubMenu2',
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
