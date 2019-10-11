# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0099_auto_20160405_1752'),
    ]

    operations = [
        migrations.CreateModel(
            name='PersonneProgramme',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_creation', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('date_last_modif', models.DateTimeField(auto_now=True, verbose_name='Last changed')),
                ('date_v_debut', models.DateTimeField(default=django.utils.timezone.now, verbose_name='V. start')),
                ('date_v_fin', models.DateTimeField(default=None, null=True, verbose_name='V. end', blank=True)),
                ('personne', models.ForeignKey(verbose_name='Person', to='app.Personne')),
                ('programme', models.ForeignKey(verbose_name='Program', to='app.TagTraduit')),
            ],
            options={
                'ordering': ['date_v_debut'],
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='tagbase',
            name='type_tag',
            field=models.IntegerField(default=None, null=True, blank=True, choices=[(1, 'Program'), (2, 'Activities'), (3, 'Hobbies'), (4, 'Driving licences'), (5, 'Personality'), (6, 'Language')]),
        ),
        migrations.AddField(
            model_name='personne',
            name='programmes2',
            field=models.ManyToManyField(default=None, related_name='personne_programme', through='app.PersonneProgramme', to='app.TagTraduit', blank=True),
        ),
    ]
