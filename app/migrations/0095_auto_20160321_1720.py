# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0094_auto_20160318_1850'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tagbase',
            options={'ordering': ['date_v_debut'], 'verbose_name': 'Tag r\xe9f\xe9rent', 'verbose_name_plural': 'Tags r\xe9f\xe9rents'},
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
        migrations.AlterField(
            model_name='tagtraduit',
            name='tag',
            field=models.ForeignKey(related_name='tag', default=None, blank=True, to='app.TagBase', help_text="C'est le tag r\xe9f\xe9rent", null=True),
        ),
    ]
