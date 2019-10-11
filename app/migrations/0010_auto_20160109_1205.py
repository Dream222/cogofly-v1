# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_personne_temporary_visible_password'),
    ]

    operations = [
        migrations.CreateModel(
            name='PersonneRelation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_creation', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('date_last_modif', models.DateTimeField(auto_now=True, verbose_name='Last changed')),
                ('date_v_debut', models.DateTimeField(default=django.utils.timezone.now, verbose_name='V. start')),
                ('date_v_fin', models.DateTimeField(default=None, null=True, verbose_name='V. end', blank=True)),
                ('type_relation', models.CharField(default='2', max_length=1, choices=[('1', 'Mari <> femme'), ('0', 'Parent > enfant'), ('2', 'Professeur > \xe9l\xe8ve')])),
                ('is_reverse', models.BooleanField(default=False)),
                ('dst', models.ForeignKey(related_name='dst', to='app.Personne')),
                ('opposite', models.ForeignKey(default=None, blank=True, to='app.PersonneRelation', null=True)),
                ('src', models.ForeignKey(related_name='src', to='app.Personne')),
            ],
            options={
                'verbose_name': 'Relation',
                'verbose_name_plural': 'Relations',
            },
        ),
        migrations.AddField(
            model_name='personne',
            name='relations',
            field=models.ManyToManyField(to='app.Personne', through='app.PersonneRelation'),
        ),
    ]
