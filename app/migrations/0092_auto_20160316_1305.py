# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0091_tagbase_tagtraduit'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tagtraduit',
            name='langue',
        ),
        migrations.RemoveField(
            model_name='tagtraduit',
            name='tag',
        ),
        migrations.DeleteModel(
            name='TagBase',
        ),
        migrations.DeleteModel(
            name='TagTraduit',
        ),
    ]
