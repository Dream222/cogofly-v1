# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0126_auto_20160518_1922'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='conversation',
            options={'ordering': ['date_v_debut']},
        ),
        migrations.AlterOrderWithRespectTo(
            name='conversation',
            order_with_respect_to=None,
        ),
    ]
