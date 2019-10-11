# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0181_auto_20160707_1330'),
    ]

    operations = [
        migrations.AddField(
            model_name='personne',
            name='newsletter_configuration',
            field=models.IntegerField(default=2, null=True, blank=True, choices=[(1, 'Every new event'), (2, 'Every week'), (3, 'Every month'), (4, 'Never send news')]),
        ),
    ]
