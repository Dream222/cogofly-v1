# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0063_auto_20160226_1930'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='message',
            options={'ordering': ['date_creation']},
        ),
    ]
