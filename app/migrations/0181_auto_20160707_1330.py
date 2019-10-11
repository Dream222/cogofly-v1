# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0180_personne_site_url'),
    ]

    operations = [
        migrations.RenameField(
            model_name='personne',
            old_name='site_url',
            new_name='site_web',
        ),
    ]
