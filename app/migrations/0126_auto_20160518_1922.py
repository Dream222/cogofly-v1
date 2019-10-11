# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0125_auto_20160416_0032'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='conversation',
            options={},
        ),
        migrations.AlterOrderWithRespectTo(
            name='conversation',
            order_with_respect_to='messages',
        ),
    ]
