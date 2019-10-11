# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0148_auto_20160602_1741'),
    ]

    operations = [
        migrations.RenameField(
            model_name='activitecomments',
            old_name='activite',
            new_name='activite_dst',
        ),
        migrations.RemoveField(
            model_name='activite',
            name='comments',
        ),
        migrations.RemoveField(
            model_name='activitecomments',
            name='activite_comment',
        ),
        migrations.AddField(
            model_name='activite',
            name='comment',
            field=models.ForeignKey(related_name='activite', default=None, blank=True, to='app.ActiviteComments', null=True),
        ),
        migrations.AlterField(
            model_name='activite',
            name='activite',
            field=models.IntegerField(default=0, choices=[(0, 'has a new relationship:'), (1, 'has a new travel:'), (2, "has changed a travel, it's now:"), (3, "Cogofly's news"), (4, 'has made a comment:')]),
        ),
        migrations.AlterField(
            model_name='activitecomments',
            name='personne',
            field=models.ForeignKey(related_name='personne', blank=True, to='app.Personne', null=True),
        ),
    ]
