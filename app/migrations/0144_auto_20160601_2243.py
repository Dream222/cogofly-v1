# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0143_personne_est_active'),
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
        migrations.AddField(
            model_name='conversation',
            name='cacas',
            field=models.ManyToManyField(related_name='conversations', to='app.Personne'),
        ),
        migrations.AddField(
            model_name='message',
            name='dst_visible',
            field=models.BooleanField(default=True, verbose_name='Visible by dst'),
        ),
        migrations.AddField(
            model_name='message',
            name='src_visible',
            field=models.BooleanField(default=True, verbose_name='Visible by src'),
        ),
        migrations.DeleteModel(
            name='ConversationPersonne',
        ),
    ]
