# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0103_auto_20160406_1707'),
    ]

    operations = [
        migrations.RenameField(
            model_name='personne',
            old_name='personnalite2',
            new_name='personnalites2',
        ),
    ]
