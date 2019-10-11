# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0170_auto_20160617_1902'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activitetestimony',
            name='testimony_show_name',
            field=models.BooleanField(default=False, help_text='Shows the name and profile picture inside the testimony page', verbose_name='Show name and picture'),
        ),
    ]
