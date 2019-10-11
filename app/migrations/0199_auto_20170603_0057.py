# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0198_message_dst_message_unread_notification'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='dst_message_unread_notification',
            new_name='dst_message_unread_notified',
        ),
    ]
