# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0085_auto_20160314_1553'),
    ]

    operations = [
        migrations.CreateModel(
            name='PersonneThrough',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('app.conversation_personnes',),
        ),
    ]
