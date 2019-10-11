# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0135_auto_20160524_2212'),
    ]

    operations = [
        migrations.AddField(
            model_name='activite',
            name='shared',
            field=models.ForeignKey(related_name='shared_activity', default=None, blank=True, to='app.Activite', null=True, verbose_name='Shared activity'),
        ),
    ]
