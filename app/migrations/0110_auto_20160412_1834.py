# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0109_auto_20160412_1731'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='taggooglemaps',
            options={'ordering': ['date_v_debut'], 'verbose_name': 'Tag google maps referent', 'verbose_name_plural': 'Tags google maps referents'},
        ),
    ]
