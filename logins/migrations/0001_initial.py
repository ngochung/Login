# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-06 04:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('phone', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=20, verbose_name='Password')),
                ('access_token', models.TextField(max_length=50)),
                ('name', models.TextField(max_length=50, verbose_name='Name')),
                ('birthday', models.DateTimeField(verbose_name='Ngày sinh')),
                ('email', models.TextField(max_length=20, verbose_name='Email')),
                ('role', models.IntegerField(verbose_name='Phân quyền')),
            ],
        ),
    ]
