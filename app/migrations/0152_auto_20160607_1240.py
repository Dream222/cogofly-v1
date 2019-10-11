# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0151_auto_20160607_0905'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActiviteShared',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_creation', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('date_last_modif', models.DateTimeField(auto_now=True, verbose_name='Last changed')),
                ('date_v_debut', models.DateTimeField(default=django.utils.timezone.now, verbose_name='V. start')),
                ('date_v_fin', models.DateTimeField(default=None, null=True, verbose_name='V. end', blank=True)),
                ('dst', models.ForeignKey(related_name='shared_to', default=None, blank=True, to='app.Personne', null=True, verbose_name='Shared to')),
                ('src', models.ForeignKey(related_name='shared_by', default=None, blank=True, to='app.Personne', null=True, verbose_name='Shared by')),
            ],
            options={
                'ordering': ['-date_last_modif'],
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='activite',
            name='shared',
        ),
        migrations.RemoveField(
            model_name='activite',
            name='shared_dst',
        ),
        migrations.RemoveField(
            model_name='activite',
            name='shared_src',
        ),
    ]
