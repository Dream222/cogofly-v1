# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_auto_20160112_1233'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mur',
            options={'ordering': ['-date_last_modif']},
        ),
    ]
