# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0138_personne_reactivate_code'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConversationPersonne',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_creation', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('date_last_modif', models.DateTimeField(auto_now=True, verbose_name='Last changed')),
                ('date_v_debut', models.DateTimeField(default=django.utils.timezone.now, verbose_name='V. start')),
                ('date_v_fin', models.DateTimeField(default=None, null=True, verbose_name='V. end', blank=True)),
                ('visible', models.BooleanField(default=True, verbose_name='Message visible')),
            ],
            options={
                'ordering': ['date_v_debut'],
                'abstract': False,
            },
        ),
        migrations.DeleteModel(
            name='PersonneThrough',
        ),
        migrations.RemoveField(
            model_name='conversation',
            name='personnes',
        ),
        migrations.AddField(
            model_name='conversationpersonne',
            name='conversation',
            field=models.ForeignKey(to='app.Conversation'),
        ),
        migrations.AddField(
            model_name='conversationpersonne',
            name='personne',
            field=models.ForeignKey(to='app.Personne'),
        ),
        migrations.AddField(
            model_name='conversation',
            name='connards',
            field=models.ManyToManyField(related_name='conversations', through='app.ConversationPersonne', to='app.Personne'),
        ),
    ]
