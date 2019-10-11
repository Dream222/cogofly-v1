# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0052_auto_20160224_2317'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActiviteComments',
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
        migrations.RemoveField(
            model_name='personnecomments',
            name='activite',
        ),
        migrations.RemoveField(
            model_name='personnecomments',
            name='dst',
        ),
        migrations.RemoveField(
            model_name='personnecomments',
            name='src',
        ),
        migrations.RemoveField(
            model_name='personne',
            name='comments',
        ),
        migrations.DeleteModel(
            name='PersonneComments',
        ),
        migrations.AddField(
            model_name='activitecomments',
            name='personne',
            field=models.ForeignKey(related_name='comment_personne', to='app.Personne'),
        ),
        migrations.AddField(
            model_name='activite',
            name='comments',
            field=models.ManyToManyField(related_name='activite_comments', through='app.ActiviteComments', to='app.Activite'),
        ),
    ]
