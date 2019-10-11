# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0053_auto_20160225_0026'),
    ]

    operations = [
        migrations.CreateModel(
            name='Conversation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_creation', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('date_last_modif', models.DateTimeField(auto_now=True, verbose_name='Last changed')),
                ('date_v_debut', models.DateTimeField(default=django.utils.timezone.now, verbose_name='V. start')),
                ('date_v_fin', models.DateTimeField(default=None, null=True, verbose_name='V. end', blank=True)),
            ],
            options={
                'ordering': ['date_v_debut'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ConversationPersonne',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_creation', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('date_last_modif', models.DateTimeField(auto_now=True, verbose_name='Last changed')),
                ('date_v_debut', models.DateTimeField(default=django.utils.timezone.now, verbose_name='V. start')),
                ('date_v_fin', models.DateTimeField(default=None, null=True, verbose_name='V. end', blank=True)),
                ('conversation', models.ForeignKey(to='app.Conversation')),
                ('personne', models.ForeignKey(to='app.Personne')),
            ],
            options={
                'ordering': ['date_v_debut'],
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='conversation',
            name='personnes',
            field=models.ManyToManyField(related_name='personne_conversation', through='app.ConversationPersonne', to='app.Personne', blank=True),
        ),
    ]
