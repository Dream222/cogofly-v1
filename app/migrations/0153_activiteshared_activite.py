# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0152_auto_20160607_1240'),
    ]

    operations = [
        migrations.AddField(
            model_name='activiteshared',
            name='activite',
            field=models.ForeignKey(default=None, blank=True, to='app.Activite', null=True, verbose_name='Activity'),
        ),
    ]
