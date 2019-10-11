# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0104_auto_20160406_1709'),
    ]

    operations = [
        migrations.CreateModel(
            name='PersonneLangue',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_creation', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('date_last_modif', models.DateTimeField(auto_now=True, verbose_name='Last changed')),
                ('date_v_debut', models.DateTimeField(default=django.utils.timezone.now, verbose_name='V. start')),
                ('date_v_fin', models.DateTimeField(default=None, null=True, verbose_name='V. end', blank=True)),
                ('langue', models.ForeignKey(verbose_name='Language', to='app.TagTraduit')),
                ('personne', models.ForeignKey(verbose_name='Person', to='app.Personne')),
            ],
            options={
                'ordering': ['date_v_debut'],
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='personne',
            name='langues2',
            field=models.ManyToManyField(default=None, related_name='personne_langue', through='app.PersonneLangue', to='app.TagTraduit', blank=True),
        ),
    ]
