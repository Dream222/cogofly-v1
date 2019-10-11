# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0057_conversation_personnes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='conversation',
        ),
        migrations.AddField(
            model_name='conversation',
            name='messages',
            field=models.ManyToManyField(to='app.Message'),
        ),
    ]
