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
            name='Game',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('s_time', models.DateTimeField(auto_now_add=True)),
                ('l_active', models.DateTimeField(auto_now=True)),
                ('f_p', models.ForeignKey(related_name='games_f_p', to=settings.AUTH_USER_MODEL)),
                ('n_to_m', models.ForeignKey(related_name='games_to_m', to=settings.AUTH_USER_MODEL)),
                ('s_p', models.ForeignKey(related_name='games_s_p', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Move',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('x', models.IntegerField()),
                ('y', models.IntegerField()),
                ('comment', models.CharField(max_length=300)),
                ('game', models.ForeignKey(to='ttt.Game')),
            ],
        ),
    ]
