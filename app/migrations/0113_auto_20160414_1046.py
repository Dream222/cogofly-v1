# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0112_taggooglemapstraduit_tag_google_maps'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='taggooglemaps',
            name='tagbase_ptr',
        ),
        migrations.RemoveField(
            model_name='taggooglemapstraduit',
            name='langue',
        ),
        migrations.RemoveField(
            model_name='taggooglemapstraduit',
            name='tag_google_maps',
        ),
        migrations.RemoveField(
            model_name='taggooglemapstraduit',
            name='taggooglemaps_ptr',
        ),
        migrations.DeleteModel(
            name='TagGoogleMaps',
        ),
        migrations.DeleteModel(
            name='TagGoogleMapsTraduit',
        ),
    ]
