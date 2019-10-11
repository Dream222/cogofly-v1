# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0077_auto_20160303_1545'),
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
