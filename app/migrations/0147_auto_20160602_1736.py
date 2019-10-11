# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0146_personnethrough'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activite',
            name='comments',
            field=models.ManyToManyField(related_name='activites', through='app.ActiviteComments', to='app.Activite'),
        ),
    ]
