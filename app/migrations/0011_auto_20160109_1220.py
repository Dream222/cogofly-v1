# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_auto_20160109_1205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personnerelation',
            name='type_relation',
            field=models.CharField(default='3', max_length=1, choices=[('1', 'Mari <> femme'), ('0', 'Parent > enfant'), ('3', 'Ami(e) <> ami(e)'), ('2', 'Professeur > \xe9l\xe8ve')]),
        ),
    ]
