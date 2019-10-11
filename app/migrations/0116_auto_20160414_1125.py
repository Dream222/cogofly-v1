# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0115_auto_20160414_1120'),
    ]

    operations = [
        migrations.RenameField(
            model_name='personnetravel2',
            old_name='travel',
            new_name='travel2',
        ),
    ]
