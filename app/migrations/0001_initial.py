# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Langue',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_creation', models.DateTimeField(auto_now_add=True)),
                ('date_last_modif', models.DateTimeField(auto_now=True)),
                ('date_v_debut', models.DateTimeField(default=django.utils.timezone.now, verbose_name='V. start')),
                ('date_v_fin', models.DateTimeField(default=None, null=True, verbose_name='V. end', blank=True)),
                ('nom', models.CharField(max_length=50)),
                ('nom_local', models.CharField(default=b'', max_length=50)),
                ('locale', models.CharField(max_length=2)),
                ('bidirectionnel', models.BooleanField(default=False)),
                ('active', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['date_v_debut'],
                'abstract': False,
                'verbose_name_plural': 'Langues',
            },
        ),
        migrations.CreateModel(
            name='Personne',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_creation', models.DateTimeField(auto_now_add=True)),
                ('date_last_modif', models.DateTimeField(auto_now=True)),
                ('date_v_debut', models.DateTimeField(default=django.utils.timezone.now, verbose_name='V. start')),
                ('date_v_fin', models.DateTimeField(default=None, null=True, verbose_name='V. end', blank=True)),
                ('sexe', models.CharField(default='0', max_length=1, choices=[('1', 'Female'), ('0', 'Male')])),
                ('nb_enfants', models.IntegerField(default=0, blank=True)),
                ('statut', models.CharField(default='0', max_length=1, choices=[('1', 'Married'), ('0', 'Single'), ('2', 'Divorced')])),
                ('est_fumeur', models.CharField(default='0', max_length=1, null=True, blank=True, choices=[('1', 'Smoker'), ('0', 'Non-smoker')])),
                ('est_physique', models.BooleanField(default=True)),
                ('confirmation_code', models.CharField(default='', max_length=200, blank=True)),
                ('champs_supplementaires', models.TextField(default=None, null=True, blank=True)),
                ('date_naissance', models.DateField(default=None, null=True, verbose_name='Birth date', blank=True)),
            ],
            options={
                'ordering': ['date_v_debut'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PersonneCentreDInteret',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_creation', models.DateTimeField(auto_now_add=True)),
                ('date_last_modif', models.DateTimeField(auto_now=True)),
                ('date_v_debut', models.DateTimeField(default=django.utils.timezone.now, verbose_name='V. start')),
                ('date_v_fin', models.DateTimeField(default=None, null=True, verbose_name='V. end', blank=True)),
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
            ],
            options={
                'ordering': ['date_v_debut'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PersonnePhoto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_creation', models.DateTimeField(auto_now_add=True)),
                ('date_last_modif', models.DateTimeField(auto_now=True)),
                ('date_v_debut', models.DateTimeField(default=django.utils.timezone.now, verbose_name='V. start')),
                ('date_v_fin', models.DateTimeField(default=None, null=True, verbose_name='V. end', blank=True)),
                ('photo_type', models.CharField(default='0', max_length=1, choices=[('1', 'Travel'), ('0', 'Profil')])),
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
            ],
            options={
                'ordering': ['date_v_debut'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_creation', models.DateTimeField(auto_now_add=True)),
                ('date_last_modif', models.DateTimeField(auto_now=True)),
                ('date_v_debut', models.DateTimeField(default=django.utils.timezone.now, verbose_name='V. start')),
                ('date_v_fin', models.DateTimeField(default=None, null=True, verbose_name='V. end', blank=True)),
                ('image', models.ImageField(null=True, upload_to=b'')),
            ],
            options={
                'ordering': ['date_v_debut'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_creation', models.DateTimeField(auto_now_add=True)),
                ('date_last_modif', models.DateTimeField(auto_now=True)),
                ('date_v_debut', models.DateTimeField(default=django.utils.timezone.now, verbose_name='V. start')),
                ('date_v_fin', models.DateTimeField(default=None, null=True, verbose_name='V. end', blank=True)),
                ('type_tag', models.CharField(default='0', max_length=1, choices=[('1', 'Job'), ('0', 'Enterprise'), ('3', 'Google maps'), ('2', 'Language'), ('5', 'Driving licences'), ('4', 'Driving licences'), ('7', 'Hobby'), ('6', 'Point of interest')])),
                ('description', models.CharField(default='', max_length=200, null=True, blank=True)),
                ('langue', models.ForeignKey(to='app.Langue')),
            ],
            options={
                'ordering': ['date_v_debut'],
                'abstract': False,
                'verbose_name': 'Tag',
            },
        ),
        migrations.CreateModel(
            name='TagWithValue',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_creation', models.DateTimeField(auto_now_add=True)),
                ('date_last_modif', models.DateTimeField(auto_now=True)),
                ('date_v_debut', models.DateTimeField(default=django.utils.timezone.now, verbose_name='V. start')),
                ('date_v_fin', models.DateTimeField(default=None, null=True, verbose_name='V. end', blank=True)),
                ('type_tag', models.CharField(default='0', max_length=1, choices=[('1', 'Job'), ('0', 'Enterprise'), ('3', 'Google maps'), ('2', 'Language'), ('5', 'Driving licences'), ('4', 'Driving licences'), ('7', 'Hobby'), ('6', 'Point of interest')])),
                ('description', models.CharField(default='', max_length=200, null=True, blank=True)),
                ('value', models.CharField(default='', max_length=200, null=True, blank=True)),
                ('langue', models.ForeignKey(to='app.Langue')),
            ],
            options={
                'ordering': ['date_v_debut'],
                'abstract': False,
                'verbose_name': 'Tag with an associated value',
                'verbose_name_plural': 'Tags with an associated value',
            },
        ),
        migrations.CreateModel(
            name='Texte',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_creation', models.DateTimeField(auto_now_add=True)),
                ('date_last_modif', models.DateTimeField(auto_now=True)),
                ('date_v_debut', models.DateTimeField(default=django.utils.timezone.now, verbose_name='V. start')),
                ('date_v_fin', models.DateTimeField(default=None, null=True, verbose_name='V. end', blank=True)),
                ('texte', models.CharField(max_length=200)),
                ('langue', models.ForeignKey(to='app.Langue')),
            ],
            options={
                'ordering': ['date_v_debut'],
                'abstract': False,
                'verbose_name': 'Text',
            },
        ),
        migrations.AddField(
            model_name='personnetypepermis',
            name='type_permis',
            field=models.ForeignKey(verbose_name='Licence', to='app.TagWithValue'),
        ),
        migrations.AddField(
            model_name='personnephoto',
            name='photo',
            field=models.ForeignKey(verbose_name='Picture', to='app.Photo'),
        ),
        migrations.AddField(
            model_name='personnelangue',
            name='langue',
            field=models.ForeignKey(verbose_name='Language', to='app.TagWithValue'),
        ),
        migrations.AddField(
            model_name='personnelangue',
            name='personne',
            field=models.ForeignKey(verbose_name='Person', to='app.Personne'),
        ),
        migrations.AddField(
            model_name='personnehobby',
            name='hobby',
            field=models.ForeignKey(verbose_name='Hobby', to='app.TagWithValue'),
        ),
        migrations.AddField(
            model_name='personnehobby',
            name='personne',
            field=models.ForeignKey(verbose_name='Person', to='app.Personne'),
        ),
        migrations.AddField(
            model_name='personnediplome',
            name='diplome',
            field=models.ForeignKey(verbose_name='Diploma', to='app.TagWithValue'),
        ),
        migrations.AddField(
            model_name='personnediplome',
            name='personne',
            field=models.ForeignKey(verbose_name='Person', to='app.Personne'),
        ),
        migrations.AddField(
            model_name='personnecentredinteret',
            name='centre_dinteret',
            field=models.ForeignKey(verbose_name='Point of interest', to='app.TagWithValue'),
        ),
        migrations.AddField(
            model_name='personnecentredinteret',
            name='personne',
            field=models.ForeignKey(verbose_name='Person', to='app.Personne'),
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
            name='photos',
            field=models.ManyToManyField(related_name='parent', through='app.PersonnePhoto', to='app.Photo', blank=True),
        ),
        migrations.AddField(
            model_name='personne',
            name='place_i_live',
            field=models.ForeignKey(related_name='place_i_live_tag', default=None, blank=True, to='app.Tag', null=True, verbose_name='Place I live'),
        ),
        migrations.AddField(
            model_name='personne',
            name='place_of_birth',
            field=models.ForeignKey(related_name='place_of_birth_tag', default=None, blank=True, to='app.Tag', null=True, verbose_name='Place of birth'),
        ),
        migrations.AddField(
            model_name='personne',
            name='types_permis',
            field=models.ManyToManyField(default=None, related_name='personne_type_permis', through='app.PersonneTypePermis', to='app.TagWithValue', blank=True),
        ),
        migrations.AddField(
            model_name='personne',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
        ),
    ]
