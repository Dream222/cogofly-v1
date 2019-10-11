# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0020_auto_20160119_1108'),
    ]

    operations = [
        migrations.CreateModel(
            name='PersonneLiked',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_creation', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('date_last_modif', models.DateTimeField(auto_now=True, verbose_name='Last changed')),
                ('date_v_debut', models.DateTimeField(default=django.utils.timezone.now, verbose_name='V. start')),
                ('date_v_fin', models.DateTimeField(default=None, null=True, verbose_name='V. end', blank=True)),
            ],
            options={
                'verbose_name': 'Like',
                'verbose_name_plural': 'Likes',
            },
        ),
        migrations.AlterField(
            model_name='personne',
            name='relations',
            field=models.ManyToManyField(related_name='personne_relations', through='app.PersonneRelation', to='app.Personne'),
        ),
        migrations.AlterField(
            model_name='personnerelation',
            name='dst',
            field=models.ForeignKey(related_name='relation_dst', to='app.Personne'),
        ),
        migrations.AlterField(
            model_name='personnerelation',
            name='src',
            field=models.ForeignKey(related_name='relation_src', to='app.Personne'),
        ),
        migrations.AddField(
            model_name='personneliked',
            name='dst',
            field=models.ForeignKey(related_name='liked_dst', to='app.Personne'),
        ),
        migrations.AddField(
            model_name='personneliked',
            name='src',
            field=models.ForeignKey(related_name='liked_src', to='app.Personne'),
        ),
        migrations.AddField(
            model_name='personne',
            name='liked',
            field=models.ManyToManyField(related_name='personne_liked', through='app.PersonneLiked', to='app.Personne'),
        ),
    ]
