# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_auto_20160111_1257'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mur',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_creation', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('date_last_modif', models.DateTimeField(auto_now=True, verbose_name='Last changed')),
                ('date_v_debut', models.DateTimeField(default=django.utils.timezone.now, verbose_name='V. start')),
                ('date_v_fin', models.DateTimeField(default=None, null=True, verbose_name='V. end', blank=True)),
                ('relation', models.ForeignKey(verbose_name='Relationship', blank=True, to='app.PersonneRelation', null=True)),
                ('travel', models.ForeignKey(default=None, verbose_name='Travel', blank=True, to='app.TagWithValue')),
            ],
            options={
                'ordering': ['date_v_debut'],
                'abstract': False,
            },
        ),
    ]
