# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-27 05:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logins', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.IntegerField(verbose_name='Ph\xe2n Quy\u1ec1n'),
        ),
    ]