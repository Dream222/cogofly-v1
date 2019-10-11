# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0197_auto_20170209_1130'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='dst_message_unread_notification',
            field=models.DateTimeField(default=None, null=True, verbose_name='Destination is notified by mail'),
        ),
    ]
