# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0044_auto_20160222_1837'),
    ]

    operations = [
        migrations.AddField(
            model_name='personne',
            name='employer_current',
            field=models.ForeignKey(related_name='employer_current_tag', default=None, blank=True, to='app.Tag', null=True, verbose_name='Current employer'),
        ),
        migrations.AddField(
            model_name='personne',
            name='employer_past',
            field=models.ForeignKey(related_name='employer_past_tag', default=None, blank=True, to='app.Tag', null=True, verbose_name='Previous employer'),
        ),
    ]
