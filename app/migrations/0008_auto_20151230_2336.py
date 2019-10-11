# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20151229_1652'),
    ]

    operations = [
        migrations.CreateModel(
            name='PersonneTravel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_creation', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('date_last_modif', models.DateTimeField(auto_now=True, verbose_name='Last changed')),
                ('date_v_debut', models.DateTimeField(default=django.utils.timezone.now, verbose_name='V. start')),
                ('date_v_fin', models.DateTimeField(default=None, null=True, verbose_name='V. end', blank=True)),
                ('date_start', models.DateTimeField(default=None, null=True, verbose_name='Start', blank=True)),
                ('date_end', models.DateTimeField(default=None, null=True, verbose_name='End', blank=True)),
                ('comments', models.TextField(null=True, verbose_name='Comments', blank=True)),
                ('personne', models.ForeignKey(verbose_name='Person', to='app.Personne')),
                ('travel', models.ForeignKey(verbose_name='Travel', to='app.TagWithValue')),
            ],
            options={
                'ordering': ['date_v_debut'],
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='personne',
            name='travels',
            field=models.ManyToManyField(default=None, related_name='personne_travel', through='app.PersonneTravel', to='app.TagWithValue', blank=True),
        ),
    ]
