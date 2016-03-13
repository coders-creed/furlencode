# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0007_auto_20160313_0022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='referrer',
            name='referrer_count',
            field=models.IntegerField(default=101),
            preserve_default=True,
        ),
    ]
