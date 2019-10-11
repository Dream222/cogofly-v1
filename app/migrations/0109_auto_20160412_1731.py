# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0108_taggooglemapstraduit_langue'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='taggooglemapstraduit',
            name='taggooglemaps_ptr',
        ),
        migrations.AddField(
            model_name='taggooglemaps',
            name='place_id',
            field=models.CharField(default='', max_length=100, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='taggooglemaps',
            name='viewport_northeast_lng',
            field=models.DecimalField(default=None, null=True, max_digits=19, decimal_places=10, blank=True),
        ),
        migrations.AddField(
            model_name='taggooglemaps',
            name='viewport_southwest_lng',
            field=models.DecimalField(default=None, null=True, max_digits=19, decimal_places=10, blank=True),
        ),
        migrations.AddField(
            model_name='taggooglemapstraduit',
            name='date_creation',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 12, 17, 30, 34, 827000), verbose_name='Created', auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='taggooglemapstraduit',
            name='date_last_modif',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 12, 17, 30, 43, 852000), verbose_name='Last changed', auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='taggooglemapstraduit',
            name='date_v_debut',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='V. start'),
        ),
        migrations.AddField(
            model_name='taggooglemapstraduit',
            name='date_v_fin',
            field=models.DateTimeField(default=None, null=True, verbose_name='V. end', blank=True),
        ),
        migrations.AddField(
            model_name='taggooglemapstraduit',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, default=None, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='taggooglemapstraduit',
            name='tag_google_maps',
            field=models.ForeignKey(related_name='tag_google_maps', default=None, blank=True, to='app.TagGoogleMaps', help_text='Position de r\xe9f\xe9rence', null=True),
        ),
    ]
