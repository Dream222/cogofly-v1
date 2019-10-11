# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0098_auto_20160405_1736'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personne',
            name='hobbies2',
            field=models.ManyToManyField(default=None, related_name='personne_hobby', through='app.PersonneHobby', to='app.TagTraduit', blank=True),
        ),
        migrations.AlterField(
            model_name='personnehobby',
            name='hobby',
            field=models.ForeignKey(verbose_name='Hobby', to='app.TagTraduit'),
        ),
    ]
