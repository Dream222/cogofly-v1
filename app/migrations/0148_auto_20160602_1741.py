# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0147_auto_20160602_1736'),
    ]

    operations = [
        migrations.AddField(
            model_name='activitecomments',
            name='activite_comment',
            field=models.ForeignKey(related_name='activite_comment', blank=True, to='app.Activite', null=True),
        ),
        migrations.AlterField(
            model_name='activitecomments',
            name='activite',
            field=models.ForeignKey(blank=True, to='app.Activite', null=True),
        ),
    ]
