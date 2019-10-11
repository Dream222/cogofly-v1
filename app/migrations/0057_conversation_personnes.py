# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0056_auto_20160225_0105'),
    ]

    operations = [
        migrations.AddField(
            model_name='conversation',
            name='personnes',
            field=models.ManyToManyField(to='app.Personne'),
        ),
    ]
