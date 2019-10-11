# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0090_auto_20160315_1733'),
    ]

    operations = [
        migrations.CreateModel(
            name='TagBase',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_creation', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('date_last_modif', models.DateTimeField(auto_now=True, verbose_name='Last changed')),
                ('date_v_debut', models.DateTimeField(default=django.utils.timezone.now, verbose_name='V. start')),
                ('date_v_fin', models.DateTimeField(default=None, null=True, verbose_name='V. end', blank=True)),
                ('type_tag', models.CharField(default='0', max_length=1, choices=[('1', 'Job'), ('0', 'Enterprise'), ('3', 'Google maps'), ('2', 'Language'), ('5', 'Diploma'), ('4', 'Driving licences'), ('7', 'Hobby'), ('6', 'Point of interest')])),
                ('description', models.CharField(default='', max_length=200, null=True, blank=True)),
            ],
            options={
                'ordering': ['date_v_debut'],
                'abstract': False,
                'verbose_name': 'Tag referent',
                'verbose_name_plural': 'Tags referents',
            },
        ),
        migrations.CreateModel(
            name='TagTraduit',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_creation', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('date_last_modif', models.DateTimeField(auto_now=True, verbose_name='Last changed')),
                ('date_v_debut', models.DateTimeField(default=django.utils.timezone.now, verbose_name='V. start')),
                ('date_v_fin', models.DateTimeField(default=None, null=True, verbose_name='V. end', blank=True)),
                ('value', models.CharField(default='', max_length=200, null=True, blank=True)),
                ('langue', models.ForeignKey(default=None, blank=True, to='app.Langue', null=True)),
                ('tag', models.ForeignKey(related_name='tag', default=None, blank=True, to='app.TagBase', null=True)),
            ],
            options={
                'ordering': ['date_v_debut'],
                'abstract': False,
                'verbose_name': 'Tag translated from a referent tag',
                'verbose_name_plural': 'Tags translated',
            },
        ),
    ]
