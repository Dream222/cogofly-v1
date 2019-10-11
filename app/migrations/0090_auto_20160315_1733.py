# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0089_taggooglemaps'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='taggooglemaps',
            name='langue',
        ),
        migrations.DeleteModel(
            name='TagGooglemaps',
        ),
    ]
