# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0045_auto_20160223_1040'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='personne',
            name='employer_past',
        ),
        migrations.AddField(
            model_name='personne',
            name='employer_previous',
            field=models.ForeignKey(related_name='employer_previous_tag', default=None, blank=True, to='app.Tag', null=True, verbose_name='Previous employer'),
        ),
    ]
