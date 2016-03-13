# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0006_auto_20160312_2226'),
    ]

    operations = [
        migrations.AddField(
            model_name='pageflow',
            name='flow_count',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='referrer',
            name='referrer_count',
            field=models.IntegerField(default=False),
            preserve_default=False,
        ),
    ]
