# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0084_messagethrough_personnethrough'),
    ]

    operations = [
        migrations.DeleteModel(
            name='MessageThrough',
        ),
        migrations.DeleteModel(
            name='PersonneThrough',
        ),
    ]
