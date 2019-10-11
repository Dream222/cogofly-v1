# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_auto_20160109_1220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personnerelation',
            name='type_relation',
            field=models.CharField(default='0', max_length=1, choices=[('1', 'Connaissance <> connaissance'), ('0', 'Ami(e) <> ami(e)'), ('3', 'Mari <> femme'), ('2', 'Parent > enfant'), ('4', 'Professeur > \xe9l\xe8ve')]),
        ),
    ]
