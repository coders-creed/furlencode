# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dashboard', '0002_companyinfo'),
    ]

    operations = [
        migrations.CreateModel(
            name='PageTime',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('page_url', models.URLField(unique=True)),
                ('page_title', models.CharField(max_length=100, blank=True)),
                ('page_time', models.IntegerField(default=0)),
                ('visit_count', models.IntegerField(default=0)),
                ('company', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
