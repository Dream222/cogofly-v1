# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0156_auto_20160608_1748'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='langue',
            options={'ordering': ['date_v_debut'], 'verbose_name_plural': 'Languages'},
        ),
        migrations.AlterField(
            model_name='activiteshared',
            name='activite',
            field=models.ForeignKey(default=None, blank=True, to='app.Activite', null=True, verbose_name='Activity sector'),
        ),
        migrations.AlterField(
            model_name='personneactivite',
            name='activite',
            field=models.ForeignKey(verbose_name='Activity sector', to='app.TagTraduit'),
        ),
        migrations.AlterField(
            model_name='personneprogramme',
            name='programme',
            field=models.ForeignKey(verbose_name='Subject', to='app.TagTraduit'),
        ),
        migrations.AlterField(
            model_name='tagbase',
            name='type_tag',
            field=models.IntegerField(default=None, null=True, blank=True, choices=[(1, 'Subjects'), (2, 'Activities'), (3, 'Hobbies'), (4, 'Driving licences'), (5, 'Personality'), (6, 'Language'), (7, 'Google maps')]),
        ),
    ]
