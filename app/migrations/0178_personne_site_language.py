# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0177_activitenewsletter'),
    ]

    operations = [
        migrations.AddField(
            model_name='personne',
            name='site_language',
            field=models.ForeignKey(related_name='site_language', default=None, blank=True, to='app.Langue', null=True, verbose_name='Language chosen in the website'),
        ),
    ]
