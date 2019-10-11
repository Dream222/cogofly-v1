# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0086_personnethrough'),
    ]

    operations = [
        migrations.CreateModel(
            name='MessageThrough',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('app.conversation_messages',),
        ),
    ]
