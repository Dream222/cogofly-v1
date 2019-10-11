# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0021_auto_20160120_1544'),
    ]

    operations = [
        migrations.AddField(
            model_name='personneliked',
            name='activite',
            field=models.ForeignKey(related_name='liked_activite', default=None, to='app.Activite'),
            preserve_default=False,
        ),
    ]
