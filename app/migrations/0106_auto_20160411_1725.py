# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0105_auto_20160406_1715'),
    ]

    operations = [
        migrations.CreateModel(
            name='TagGoogleMaps',
            fields=[
                ('tagbase_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='app.TagBase')),
                ('lat', models.DecimalField(default=None, null=True, max_digits=19, decimal_places=10, blank=True)),
                ('lng', models.DecimalField(default=None, null=True, max_digits=19, decimal_places=10, blank=True)),
                ('viewport_northeast_lat', models.DecimalField(default=None, null=True, max_digits=19, decimal_places=10, blank=True)),
                ('viewport_southwest_lat', models.DecimalField(default=None, null=True, max_digits=19, decimal_places=10, blank=True)),
            ],
            options={
                'ordering': ['date_v_debut'],
                'abstract': False,
                'verbose_name': 'Tag google maps of a place in a language',
                'verbose_name_plural': 'Tags google maps of a place in a language',
            },
            bases=('app.tagbase',),
        ),
        migrations.AlterField(
            model_name='tagbase',
            name='type_tag',
            field=models.IntegerField(default=None, null=True, blank=True, choices=[(1, 'Program'), (2, 'Activities'), (3, 'Hobbies'), (4, 'Driving licences'), (5, 'Personality'), (6, 'Language'), (7, 'Google maps')]),
        ),
        migrations.CreateModel(
            name='TagGoogleMapsTraduit',
            fields=[
                ('taggooglemaps_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='app.TagGoogleMaps')),
                ('formatted_address', models.CharField(default='', max_length=200, null=True, blank=True)),
            ],
            options={
                'ordering': ['date_v_debut'],
                'abstract': False,
                'verbose_name': 'Tag google maps of a place in a language',
                'verbose_name_plural': 'Tags google maps of a place in a language',
            },
            bases=('app.taggooglemaps',),
        ),
    ]
