# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_pagetime'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='latitude',
            field=models.FloatField(default=0.0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userinfo',
            name='longitude',
            field=models.FloatField(default=0.0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='companyinfo',
            name='domain_name',
            field=models.CharField(unique=True, max_length=50),
            preserve_default=True,
        ),
    ]
