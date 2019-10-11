# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0191_personne_reason_delete'),
    ]

    operations = [
        migrations.AddField(
            model_name='personne',
            name='one_click_login',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='personne',
            name='newsletter_configuration',
            field=models.IntegerField(default=1, null=True, blank=True, choices=[(1, 'Every day'), (2, 'Every week'), (3, 'Every month'), (4, 'Never send news')]),
        ),
    ]
