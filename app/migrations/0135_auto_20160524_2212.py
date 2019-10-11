# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0134_auto_20160524_1448'),
    ]

    operations = [
        migrations.AddField(
            model_name='activite',
            name='shared_dst',
            field=models.ForeignKey(related_name='shared_to', default=None, blank=True, to='app.Personne', null=True, verbose_name='Shared to'),
        ),
        migrations.AddField(
            model_name='activite',
            name='shared_src',
            field=models.ForeignKey(related_name='shared_by', default=None, blank=True, to='app.Personne', null=True, verbose_name='Shared by'),
        ),
    ]
