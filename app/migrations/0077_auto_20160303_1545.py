# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0076_auto_20160303_1251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personnerelation',
            name='raison_refus',
            field=models.IntegerField(default=2, null=True, blank=True, choices=[(1, 'No'), (2, 'No thank you'), (3, 'Maybe another time'), (4, 'I am quite simply not interested'), (5, 'We are quite simply not interested'), (6, 'I am not interested for now'), (7, 'We are not interested for now'), (8, 'I don\u2019t travel'), (9, 'We don\u2019t travel'), (10, 'I don\u2019t travel around'), (11, 'We don\u2019t travel around'), (12, 'I prefer to remain alone'), (13, 'We prefer to remain alone'), (14, 'We have no travel plans in common'), (15, 'We have no ideas in common for trips out'), (16, 'We have nothing in common in terms of activities'), (17, 'I don\u2019t speak your language'), (18, 'We don\u2019t speak your language'), (19, 'I don\u2019t speak English'), (20, 'We don\u2019t speak English'), (21, 'I invite you to use my contacts'), (22, 'We invite you to get in touch with our contacts'), (23, 'I invite you to contact another contact'), (24, 'We invite you to contact another person'), (25, 'I invite you to contact me by private message'), (26, 'We invite you to contact us by private message')]),
        ),
    ]
