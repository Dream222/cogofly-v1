# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0060_messagethrough'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='message_read',
            field=models.BooleanField(default=False),
        ),
    ]
