# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0174_publicite_publicitetraduit'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='publicite',
            options={'ordering': ['date_v_debut'], 'verbose_name': 'Ad', 'verbose_name_plural': 'Ads'},
        ),
        migrations.AddField(
            model_name='publicite',
            name='position',
            field=models.IntegerField(default=None, choices=[(1, 'Ads travels right'), (2, 'Ads travels left'), (3, 'Ads my profile left'), (4, 'Ads my profile right'), (5, 'Ads travels right'), (6, 'Ads travels right'), (7, 'Ads travels right'), (8, 'Ads travels right'), (9, 'Ads travels right'), (10, 'Ads travels right'), (11, 'Ads travels right')], blank=True, help_text='Where this ads goes', null=True, verbose_name='Where this ads goes'),
        ),
        migrations.AlterField(
            model_name='publicite',
            name='label',
            field=models.CharField(default=None, max_length=200, blank=True, help_text='A recall of what this ads contains (language independant)', null=True, verbose_name='Label'),
        ),
    ]
