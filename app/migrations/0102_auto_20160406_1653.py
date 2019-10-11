# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0101_auto_20160406_1625'),
    ]

    operations = [
        migrations.CreateModel(
            name='PersonneTypepermis',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_creation', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('date_last_modif', models.DateTimeField(auto_now=True, verbose_name='Last changed')),
                ('date_v_debut', models.DateTimeField(default=django.utils.timezone.now, verbose_name='V. start')),
                ('date_v_fin', models.DateTimeField(default=None, null=True, verbose_name='V. end', blank=True)),
                ('personne', models.ForeignKey(verbose_name='Person', to='app.Personne')),
                ('type_permis', models.ForeignKey(verbose_name='Licence', to='app.TagTraduit')),
            ],
            options={
                'ordering': ['date_v_debut'],
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='personne',
            name='types_permis2',
            field=models.ManyToManyField(default=None, related_name='personne_typepermis', through='app.PersonneTypepermis', to='app.TagTraduit', blank=True),
        ),
    ]
