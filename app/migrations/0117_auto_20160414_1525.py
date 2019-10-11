# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
import app.models.date_partial_field


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0116_auto_20160414_1125'),
    ]

    operations = [
        migrations.CreateModel(
            name='PersonneTravel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_creation', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('date_last_modif', models.DateTimeField(auto_now=True, verbose_name='Last changed')),
                ('date_v_debut', models.DateTimeField(default=django.utils.timezone.now, verbose_name='V. start')),
                ('date_v_fin', models.DateTimeField(default=None, null=True, verbose_name='V. end', blank=True)),
                ('comments', models.TextField(null=True, verbose_name='Comments', blank=True)),
                ('date_start', app.models.date_partial_field.DatePartialField(default=None, null=True, verbose_name='Start (m/d/Y)', blank=True)),
                ('date_end', app.models.date_partial_field.DatePartialField(default=None, null=True, verbose_name='End (m/d/Y)', blank=True)),
                ('is_past', models.BooleanField(default=False, verbose_name='This is a past travel')),
            ],
            options={
                'ordering': ['date_v_debut'],
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='personnetravel2',
            name='personne',
        ),
        migrations.RemoveField(
            model_name='personnetravel2',
            name='photo1',
        ),
        migrations.RemoveField(
            model_name='personnetravel2',
            name='photo2',
        ),
        migrations.RemoveField(
            model_name='personnetravel2',
            name='photo3',
        ),
        migrations.RemoveField(
            model_name='personnetravel2',
            name='travel2',
        ),
        migrations.RemoveField(
            model_name='personne',
            name='travels2',
        ),
        migrations.AlterField(
            model_name='activite',
            name='travel2',
            field=models.ForeignKey(default=None, blank=True, to='app.PersonneTravel', null=True, verbose_name='Travel'),
        ),
        migrations.DeleteModel(
            name='PersonneTravel2',
        ),
        migrations.AddField(
            model_name='personnetravel',
            name='personne',
            field=models.ForeignKey(verbose_name='Person', to='app.Personne'),
        ),
        migrations.AddField(
            model_name='personnetravel',
            name='photo1',
            field=models.ForeignKey(related_name='photo1', verbose_name='Travel picture 1', blank=True, to='app.Photo', null=True),
        ),
        migrations.AddField(
            model_name='personnetravel',
            name='photo2',
            field=models.ForeignKey(related_name='photo2', verbose_name='Travel picture 2', blank=True, to='app.Photo', null=True),
        ),
        migrations.AddField(
            model_name='personnetravel',
            name='photo3',
            field=models.ForeignKey(related_name='photo3', verbose_name='Travel picture 3', blank=True, to='app.Photo', null=True),
        ),
        migrations.AddField(
            model_name='personnetravel',
            name='travel2',
            field=models.ForeignKey(verbose_name='Travel', to='app.TagGoogleMapsTraduit'),
        ),
        migrations.AddField(
            model_name='personne',
            name='travels',
            field=models.ManyToManyField(default=None, related_name='personne_travel', through='app.PersonneTravel', to='app.TagGoogleMapsTraduit', blank=True),
        ),
    ]
