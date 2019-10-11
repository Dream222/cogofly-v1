# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0111_remove_taggooglemapstraduit_tag_google_maps'),
    ]

    operations = [
        migrations.AddField(
            model_name='taggooglemapstraduit',
            name='tag_google_maps',
            field=models.ForeignKey(related_name='tag_google_maps', default=None, blank=True, to='app.TagGoogleMaps', help_text='Position de r\xe9f\xe9rence', null=True),
        ),
    ]
