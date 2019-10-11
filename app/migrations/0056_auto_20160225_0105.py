# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0055_auto_20160225_0055'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='conversationpersonne',
            name='conversation',
        ),
        migrations.RemoveField(
            model_name='conversationpersonne',
            name='personne',
        ),
        migrations.RemoveField(
            model_name='conversation',
            name='personnes',
        ),
        migrations.DeleteModel(
            name='ConversationPersonne',
        ),
    ]
