# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0049_auto_20160224_1153'),
    ]

    operations = [
        migrations.CreateModel(
            name='PersonneComments',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_creation', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('date_last_modif', models.DateTimeField(auto_now=True, verbose_name='Last changed')),
                ('date_v_debut', models.DateTimeField(default=django.utils.timezone.now, verbose_name='V. start')),
                ('date_v_fin', models.DateTimeField(default=None, null=True, verbose_name='V. end', blank=True)),
                ('comment', models.TextField(null=True, verbose_name='Comment', blank=True)),
                ('activite', models.ForeignKey(related_name='comment_activite', to='app.Activite')),
            ],
            options={
                'verbose_name': 'Comment',
                'verbose_name_plural': 'Comments',
            },
        ),
        migrations.CreateModel(
            name='PersonneMessages',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_creation', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('date_last_modif', models.DateTimeField(auto_now=True, verbose_name='Last changed')),
                ('date_v_debut', models.DateTimeField(default=django.utils.timezone.now, verbose_name='V. start')),
                ('date_v_fin', models.DateTimeField(default=None, null=True, verbose_name='V. end', blank=True)),
                ('message', models.TextField(null=True, verbose_name='Message', blank=True)),
            ],
            options={
                'verbose_name': 'Message',
                'verbose_name_plural': 'Messages',
            },
        ),
        migrations.AlterField(
            model_name='personne',
            name='est_fumeur',
            field=models.IntegerField(default=0, null=True, blank=True, choices=[(0, 'Non-smoker'), (1, 'Smoker'), (2, 'Social smoker'), (3, 'Other')]),
        ),
        migrations.AlterField(
            model_name='personne',
            name='sexe',
            field=models.CharField(default=1, max_length=1, choices=[(1, 'Male'), (2, 'Female')]),
        ),
        migrations.AlterField(
            model_name='personnerelation',
            name='type_relation',
            field=models.IntegerField(default=1, choices=[(1, 'friend'), (2, 'relationship'), (3, 'parent / child'), (4, 'husband / wife'), (5, 'teacher / student')]),
        ),
        migrations.AddField(
            model_name='personnemessages',
            name='dst',
            field=models.ForeignKey(related_name='message_dst', to='app.Personne'),
        ),
        migrations.AddField(
            model_name='personnemessages',
            name='src',
            field=models.ForeignKey(related_name='message_src', to='app.Personne'),
        ),
        migrations.AddField(
            model_name='personnecomments',
            name='dst',
            field=models.ForeignKey(related_name='comment_dst', to='app.Personne'),
        ),
        migrations.AddField(
            model_name='personnecomments',
            name='src',
            field=models.ForeignKey(related_name='comment_src', to='app.Personne'),
        ),
        migrations.AddField(
            model_name='personne',
            name='comments',
            field=models.ManyToManyField(related_name='personne_comments', through='app.PersonneComments', to='app.Personne'),
        ),
        migrations.AddField(
            model_name='personne',
            name='messages',
            field=models.ManyToManyField(related_name='personne_messages', through='app.PersonneMessages', to='app.Personne'),
        ),
    ]
