# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0157_auto_20160610_1141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personneliked',
            name='activite',
            field=models.ForeignKey(related_name='liked_activite', default=None, blank=True, to='app.Activite', null=True),
        ),
    ]
