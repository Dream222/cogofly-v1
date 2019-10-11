# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0113_auto_20160414_1046'),
    ]

    operations = [
        migrations.CreateModel(
            name='TagGoogleMaps',
            fields=[
                ('tagbase_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='app.TagBase')),
                ('place_id', models.CharField(default='', max_length=100, null=True, blank=True)),
                ('lat', models.DecimalField(default=None, null=True, max_digits=19, decimal_places=10, blank=True)),
                ('lng', models.DecimalField(default=None, null=True, max_digits=19, decimal_places=10, blank=True)),
                ('viewport_northeast_lat', models.DecimalField(default=None, null=True, max_digits=19, decimal_places=10, blank=True)),
                ('viewport_northeast_lng', models.DecimalField(default=None, null=True, max_digits=19, decimal_places=10, blank=True)),
                ('viewport_southwest_lat', models.DecimalField(default=None, null=True, max_digits=19, decimal_places=10, blank=True)),
                ('viewport_southwest_lng', models.DecimalField(default=None, null=True, max_digits=19, decimal_places=10, blank=True)),
            ],
            options={
                'ordering': ['date_v_debut'],
                'abstract': False,
                'verbose_name': 'Tag google maps referent',
                'verbose_name_plural': 'Tags google maps referents',
            },
            bases=('app.tagbase',),
        ),
        migrations.CreateModel(
            name='TagGoogleMapsTraduit',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_creation', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('date_last_modif', models.DateTimeField(auto_now=True, verbose_name='Last changed')),
                ('date_v_debut', models.DateTimeField(default=django.utils.timezone.now, verbose_name='V. start')),
                ('date_v_fin', models.DateTimeField(default=None, null=True, verbose_name='V. end', blank=True)),
                ('formatted_address', models.CharField(default='', max_length=200, null=True, blank=True)),
                ('langue', models.ForeignKey(default=None, blank=True, to='app.Langue', null=True)),
                ('tag_google_maps', models.ForeignKey(related_name='tag_google_maps', default=None, blank=True, to='app.TagGoogleMaps', help_text='Position de r\xe9f\xe9rence', null=True)),
            ],
            options={
                'ordering': ['date_v_debut'],
                'abstract': False,
                'verbose_name': 'Tag google maps of a place in a language',
                'verbose_name_plural': 'Tags google maps of a place in a language',
            },
        ),
    ]
