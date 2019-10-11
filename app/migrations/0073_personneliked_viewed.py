# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0072_auto_20160302_1529'),
    ]

    operations = [
        migrations.AddField(
            model_name='personneliked',
            name='viewed',
            field=models.BooleanField(default=False),
        ),
    ]
