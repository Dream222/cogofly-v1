# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0107_auto_20160411_2013'),
    ]

    operations = [
        migrations.AddField(
            model_name='taggooglemapstraduit',
            name='langue',
            field=models.ForeignKey(default=None, blank=True, to='app.Langue', null=True),
        ),
    ]
