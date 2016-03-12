# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ClickConfig',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('selector', models.CharField(max_length=100)),
                ('events', models.CharField(default=b'click', max_length=100)),
                ('company', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ClickInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('count', models.IntegerField(default=0)),
                ('click_config', models.ForeignKey(to='dashboard.ClickConfig')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PageFlow',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('from_url', models.URLField()),
                ('from_title', models.CharField(max_length=100, blank=True)),
                ('to_url', models.URLField()),
                ('to_title', models.CharField(max_length=100, blank=True)),
                ('company', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Referrer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('referrer_url', models.URLField()),
                ('referrer_title', models.CharField(max_length=100, blank=True)),
                ('company', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_hash', models.CharField(max_length=200)),
                ('os', models.CharField(max_length=75)),
                ('screen_res', models.CharField(max_length=75)),
                ('ip_addr', models.CharField(max_length=25)),
                ('browser', models.CharField(max_length=25)),
                ('timezone', models.CharField(max_length=25)),
                ('session_start', models.DateTimeField(blank=True)),
                ('session_end', models.DateTimeField(blank=True)),
                ('company', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
