# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0194_auto_20161007_2342'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tagbase',
            options={'ordering': ['date_v_debut'], 'verbose_name': 'Referent tag', 'verbose_name_plural': 'Referent tags'},
        ),
        migrations.AddField(
            model_name='blog',
            name='date_envoi_newsletter',
            field=models.DateTimeField(default=None, help_text='Date to include this blog into the newsletter', null=True, verbose_name='If this blog is always on top', blank=True),
        ),
        migrations.AlterField(
            model_name='personne',
            name='newsletter_configuration',
            field=models.IntegerField(default=2, null=True, blank=True, choices=[(1, 'Every day'), (2, 'Every week'), (3, 'Every month'), (4, 'Never send newsletter')]),
        ),
        migrations.AlterField(
            model_name='personne',
            name='place_i_live',
            field=models.ForeignKey(related_name='place_i_live_tag', default=None, blank=True, to='app.Tag', null=True, verbose_name='City where I live'),
        ),
        migrations.AlterField(
            model_name='personnerelation',
            name='type_relation',
            field=models.IntegerField(default=0, choices=[(0, 'friend'), (1, 'relationship'), (2, 'sent an invitation'), (3, 'invitation refused'), (4, 'parent / child'), (5, 'child / parent'), (6, 'husband / wife'), (7, 'wife / husband'), (8, 'teacher / student'), (9, 'student / teacher'), (10, 'remover / removed')]),
        ),
        migrations.AlterField(
            model_name='tag',
            name='type_tag',
            field=models.CharField(default='0', max_length=1, choices=[('1', 'Job'), ('0', 'Company'), ('3', 'Google maps'), ('2', 'Language'), ('5', 'Diploma'), ('4', 'Driving licences'), ('7', 'Hobby'), ('6', 'Point of interest')]),
        ),
        migrations.AlterField(
            model_name='tagwithvalue',
            name='type_tag',
            field=models.CharField(default='0', max_length=1, choices=[('1', 'Job'), ('0', 'Company'), ('3', 'Google maps'), ('2', 'Language'), ('5', 'Diploma'), ('4', 'Driving licences'), ('7', 'Hobby'), ('6', 'Point of interest')]),
        ),
    ]
