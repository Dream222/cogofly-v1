# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0175_auto_20160701_1759'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publicite',
            name='ordre_si_top',
            field=models.IntegerField(default=None, help_text='Priority: the lowest the higher ("1" is <b>before</b> "2" and so on...).', null=True, verbose_name='How this ad appears', blank=True),
        ),
        migrations.AlterField(
            model_name='publicite',
            name='position',
            field=models.IntegerField(default=None, choices=[(1, 'Ads travels right'), (2, 'Ads travels left'), (3, 'Ads my profile left'), (4, 'Ads my profile right'), (5, 'Ads news left'), (6, 'Ads news right')], blank=True, help_text='Where this ads goes', null=True, verbose_name='Where this ads goes'),
        ),
    ]
