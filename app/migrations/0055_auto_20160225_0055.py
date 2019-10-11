# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0054_auto_20160225_0051'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_creation', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('date_last_modif', models.DateTimeField(auto_now=True, verbose_name='Last changed')),
                ('date_v_debut', models.DateTimeField(default=django.utils.timezone.now, verbose_name='V. start')),
                ('date_v_fin', models.DateTimeField(default=None, null=True, verbose_name='V. end', blank=True)),
                ('message', models.TextField(null=True, verbose_name='Message', blank=True)),
                ('conversation', models.ForeignKey(to='app.Conversation')),
            ],
            options={
                'ordering': ['date_v_debut'],
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='personnemessages',
            name='dst',
        ),
        migrations.RemoveField(
            model_name='personnemessages',
            name='src',
        ),
        migrations.RemoveField(
            model_name='personne',
            name='messages',
        ),
        migrations.DeleteModel(
            name='PersonneMessages',
        ),
        migrations.AddField(
            model_name='message',
            name='dst',
            field=models.ForeignKey(related_name='message_dst', to='app.Personne'),
        ),
        migrations.AddField(
            model_name='message',
            name='src',
            field=models.ForeignKey(related_name='message_src', to='app.Personne'),
        ),
    ]
