# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0144_auto_20160601_2243'),
    ]

    operations = [
        migrations.RenameField(
            model_name='conversation',
            old_name='cacas',
            new_name='personnes',
        ),
    ]
