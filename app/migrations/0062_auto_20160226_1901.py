# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0061_message_message_read'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='message_read',
            new_name='is_read',
        ),
    ]
