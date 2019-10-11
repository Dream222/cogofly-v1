# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0019_auto_20160119_0003'),
    ]

    operations = [
        migrations.CreateModel(
            name='Activite',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_creation', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('date_last_modif', models.DateTimeField(auto_now=True, verbose_name='Last changed')),
                ('date_v_debut', models.DateTimeField(default=django.utils.timezone.now, verbose_name='V. start')),
                ('date_v_fin', models.DateTimeField(default=None, null=True, verbose_name='V. end', blank=True)),
                ('activite', models.CharField(default='0', max_length=1, choices=[('1', 'has a new travel:'), ('0', 'has a new relationship:'), ('2', "has changed a travel, it's now:")])),
                ('relation', models.ForeignKey(default=None, blank=True, to='app.PersonneRelation', null=True, verbose_name='Relationship')),
                ('travel', models.ForeignKey(default=None, blank=True, to='app.PersonneTravel', null=True, verbose_name='Travel')),
            ],
            options={
                'ordering': ['-date_last_modif'],
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='mur',
            name='relation',
        ),
        migrations.RemoveField(
            model_name='mur',
            name='travel',
        ),
        migrations.DeleteModel(
            name='Mur',
        ),
    ]
