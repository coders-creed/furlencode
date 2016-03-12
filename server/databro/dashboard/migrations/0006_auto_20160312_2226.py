# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0005_auto_20160312_2129'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userinfo',
            name='session_end',
        ),
        migrations.RemoveField(
            model_name='userinfo',
            name='session_start',
        ),
    ]
