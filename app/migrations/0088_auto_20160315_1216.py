# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0087_messagethrough'),
    ]

    operations = [
        migrations.CreateModel(
            name='PersonneHobby',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_creation', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('date_last_modif', models.DateTimeField(auto_now=True, verbose_name='Last changed')),
                ('date_v_debut', models.DateTimeField(default=django.utils.timezone.now, verbose_name='V. start')),
                ('date_v_fin', models.DateTimeField(default=None, null=True, verbose_name='V. end', blank=True)),
                ('hobby', models.ForeignKey(verbose_name='Hobby', to='app.TagWithValue')),
                ('personne', models.ForeignKey(verbose_name='Person', to='app.Personne')),
            ],
            options={
                'ordering': ['date_v_debut'],
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='personne',
            name='hobbies2',
            field=models.ManyToManyField(default=None, related_name='personne_hobby', through='app.PersonneHobby', to='app.TagWithValue', blank=True),
        ),
    ]
