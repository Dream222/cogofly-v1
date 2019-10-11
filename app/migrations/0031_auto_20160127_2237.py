# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0030_auto_20160127_2142'),
    ]

    operations = [
        migrations.RenameField(
            model_name='personnetravel',
            old_name='new_end',
            new_name='date_end',
        ),
        migrations.RenameField(
            model_name='personnetravel',
            old_name='new_start',
            new_name='date_start',
        ),
    ]
