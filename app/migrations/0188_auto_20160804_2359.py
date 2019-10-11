# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0187_auto_20160726_1212'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActiviteExpressyourself',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_creation', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('date_last_modif', models.DateTimeField(auto_now=True, verbose_name='Last changed')),
                ('date_v_debut', models.DateTimeField(default=django.utils.timezone.now, verbose_name='V. start')),
                ('date_v_fin', models.DateTimeField(default=None, null=True, verbose_name='V. end', blank=True)),
                ('message', models.TextField(null=True, verbose_name='Message', blank=True)),
                ('personne', models.ForeignKey(related_name='personne_expressyourself', blank=True, to='app.Personne', null=True)),
            ],
            options={
                'ordering': ['-date_last_modif'],
                'verbose_name': 'Activity / express yourself',
                'verbose_name_plural': 'Activities / express yourself',
            },
        ),
        migrations.AlterField(
            model_name='activite',
            name='activite',
            field=models.IntegerField(default=0, choices=[(0, 'has a new relationship:'), (1, 'has a new travel:'), (2, "has changed a travel, it's now:"), (3, "Cogofly's news"), (4, 'has made a comment:'), (5, 'has made a testimony:'), (6, 'has expressed this:')]),
        ),
        migrations.AddField(
            model_name='activite',
            name='express_yourself',
            field=models.ForeignKey(related_name='activite', default=None, blank=True, to='app.ActiviteExpressyourself', null=True),
        ),
    ]
