# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0188_auto_20160804_2359'),
    ]

    operations = [
        migrations.CreateModel(
            name='PersonneSearch',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_creation', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('date_last_modif', models.DateTimeField(auto_now=True, verbose_name='Last changed')),
                ('date_v_debut', models.DateTimeField(default=django.utils.timezone.now, verbose_name='V. start')),
                ('date_v_fin', models.DateTimeField(default=None, null=True, verbose_name='V. end', blank=True)),
                ('personne', models.ForeignKey(verbose_name='Person', to='app.Personne')),
                ('search', models.ForeignKey(verbose_name='Search', to='app.TagGoogleMapsTraduit')),
            ],
            options={
                'ordering': ['date_v_debut'],
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='blog',
            name='ordre_si_top',
            field=models.IntegerField(default=None, help_text='Priority: the higher first ("2" is <b>before</b> "1" and so on...).<br /><b>Let it blank if you don\'t want this blog on top</b>', null=True, verbose_name='If this blog is always on top', blank=True),
        ),
    ]
