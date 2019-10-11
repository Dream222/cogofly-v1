# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0182_personne_newsletter_configuration'),
    ]

    operations = [
        migrations.AddField(
            model_name='personne',
            name='newsletter_date_sent',
            field=models.DateTimeField(default=None, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='personne',
            name='newsletter_configuration',
            field=models.IntegerField(default=2, null=True, blank=True, choices=[(1, 'Every day'), (2, 'Every week'), (3, 'Every month'), (4, 'Never send news')]),
        ),
    ]
