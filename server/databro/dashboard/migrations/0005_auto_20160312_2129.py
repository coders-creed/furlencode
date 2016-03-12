# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_auto_20160312_2051'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userinfo',
            name='timezone',
        ),
        migrations.AddField(
            model_name='userinfo',
            name='mobile',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='latitude',
            field=models.FloatField(blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='longitude',
            field=models.FloatField(blank=True),
            preserve_default=True,
        ),
    ]
