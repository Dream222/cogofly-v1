# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0196_auto_20170209_1047'),
    ]

    operations = [
        migrations.CreateModel(
            name='PersonneBlogNewsletter',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_creation', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('date_last_modif', models.DateTimeField(auto_now=True, verbose_name='Last changed')),
                ('date_v_debut', models.DateTimeField(default=django.utils.timezone.now, verbose_name='V. start')),
                ('date_v_fin', models.DateTimeField(default=None, null=True, verbose_name='V. end', blank=True)),
                ('date_sent', models.DateTimeField(default=None, null=True, verbose_name='Sent', blank=True)),
            ],
            options={
                'ordering': ['-date_last_modif', '-date_v_debut'],
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='blog',
            name='date_envoi_newsletter',
            field=models.DateField(default=None, help_text='Blank = never sent. If the date is older than now it will be sent tonight.', null=True, verbose_name='Add this blog into the newsletter', blank=True),
        ),
        migrations.AddField(
            model_name='personneblognewsletter',
            name='blog',
            field=models.ForeignKey(default=None, blank=True, to='app.Blog', null=True, verbose_name='Blog'),
        ),
        migrations.AddField(
            model_name='personneblognewsletter',
            name='personne',
            field=models.ForeignKey(default=None, blank=True, to='app.Personne', null=True, verbose_name='To'),
        ),
    ]
