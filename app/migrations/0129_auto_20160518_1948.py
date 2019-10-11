# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0128_auto_20160518_1946'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conversation',
            name='messages',
            field=models.ManyToManyField(related_name='conversations', to='app.Message'),
        ),
        migrations.AlterField(
            model_name='conversation',
            name='personnes',
            field=models.ManyToManyField(related_name='conversations', to='app.Personne'),
        ),
    ]
