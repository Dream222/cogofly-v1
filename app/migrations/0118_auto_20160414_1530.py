# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0117_auto_20160414_1525'),
    ]

    operations = [
        migrations.RenameField(
            model_name='activite',
            old_name='travel2',
            new_name='travel',
        ),
        migrations.RenameField(
            model_name='personnetravel',
            old_name='travel2',
            new_name='travel',
        ),
    ]
