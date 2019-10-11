# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0195_auto_20170209_1011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='date_envoi_newsletter',
            field=models.DateTimeField(default=None, help_text='Blank = never sent. You can set date in the future.', null=True, verbose_name='When to add this blog into the newsletter', blank=True),
        ),
    ]
