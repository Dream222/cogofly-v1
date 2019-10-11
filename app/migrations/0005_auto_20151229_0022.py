# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20151229_0019'),
    ]

    operations = [
        migrations.CreateModel(
            name='PersonneCentreDInteret',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_creation', models.DateTimeField(auto_now_add=True)),
                ('date_last_modif', models.DateTimeField(auto_now=True)),
                ('date_v_debut', models.DateTimeField(default=django.utils.timezone.now, verbose_name='V. start')),
                ('date_v_fin', models.DateTimeField(default=None, null=True, verbose_name='V. end', blank=True)),
                ('centre_dinteret', models.ForeignKey(verbose_name='Point of interest', to='app.TagWithValue')),
                ('personne', models.ForeignKey(verbose_name='Person', to='app.Personne')),
            ],
            options={
                'ordering': ['date_v_debut'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PersonneDiplome',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_creation', models.DateTimeField(auto_now_add=True)),
                ('date_last_modif', models.DateTimeField(auto_now=True)),
                ('date_v_debut', models.DateTimeField(default=django.utils.timezone.now, verbose_name='V. start')),
                ('date_v_fin', models.DateTimeField(default=None, null=True, verbose_name='V. end', blank=True)),
                ('diplome', models.ForeignKey(verbose_name='Diploma', to='app.TagWithValue')),
                ('personne', models.ForeignKey(verbose_name='Person', to='app.Personne')),
            ],
            options={
                'ordering': ['date_v_debut'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PersonneHobby',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_creation', models.DateTimeField(auto_now_add=True)),
                ('date_last_modif', models.DateTimeField(auto_now=True)),
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
        migrations.CreateModel(
            name='PersonneLangue',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_creation', models.DateTimeField(auto_now_add=True)),
                ('date_last_modif', models.DateTimeField(auto_now=True)),
                ('date_v_debut', models.DateTimeField(default=django.utils.timezone.now, verbose_name='V. start')),
                ('date_v_fin', models.DateTimeField(default=None, null=True, verbose_name='V. end', blank=True)),
                ('langue', models.ForeignKey(verbose_name='Language', to='app.TagWithValue')),
                ('personne', models.ForeignKey(verbose_name='Person', to='app.Personne')),
            ],
            options={
                'ordering': ['date_v_debut'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PersonneTypePermis',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_creation', models.DateTimeField(auto_now_add=True)),
                ('date_last_modif', models.DateTimeField(auto_now=True)),
                ('date_v_debut', models.DateTimeField(default=django.utils.timezone.now, verbose_name='V. start')),
                ('date_v_fin', models.DateTimeField(default=None, null=True, verbose_name='V. end', blank=True)),
                ('personne', models.ForeignKey(verbose_name='Person', to='app.Personne')),
                ('type_permis', models.ForeignKey(verbose_name='Licence', to='app.TagWithValue')),
            ],
            options={
                'ordering': ['date_v_debut'],
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='personne',
            name='centres_dinteret',
            field=models.ManyToManyField(default=None, related_name='personne_centres_dinteret', through='app.PersonneCentreDInteret', to='app.TagWithValue', blank=True),
        ),
        migrations.AddField(
            model_name='personne',
            name='diplomes',
            field=models.ManyToManyField(default=None, related_name='personne_diplome', through='app.PersonneDiplome', to='app.TagWithValue', blank=True),
        ),
        migrations.AddField(
            model_name='personne',
            name='hobbies',
            field=models.ManyToManyField(default=None, related_name='personne_hobby', through='app.PersonneHobby', to='app.TagWithValue', blank=True),
        ),
        migrations.AddField(
            model_name='personne',
            name='langues',
            field=models.ManyToManyField(default=None, related_name='personne_langue', through='app.PersonneLangue', to='app.TagWithValue', blank=True),
        ),
        migrations.AddField(
            model_name='personne',
            name='types_permis',
            field=models.ManyToManyField(default=None, related_name='personne_type_permis', through='app.PersonneTypePermis', to='app.TagWithValue', blank=True),
        ),
    ]
