# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20151229_0028'),
    ]

    operations = [
        migrations.AddField(
            model_name='personne',
            name='self_description',
            field=models.TextField(null=True, verbose_name='Describe yourself', blank=True),
        ),
        migrations.AlterField(
            model_name='langue',
            name='date_creation',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Created'),
        ),
        migrations.AlterField(
            model_name='langue',
            name='date_last_modif',
            field=models.DateTimeField(auto_now=True, verbose_name='Last changed'),
        ),
        migrations.AlterField(
            model_name='personne',
            name='date_creation',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Created'),
        ),
        migrations.AlterField(
            model_name='personne',
            name='date_last_modif',
            field=models.DateTimeField(auto_now=True, verbose_name='Last changed'),
        ),
        migrations.AlterField(
            model_name='personnecentredinteret',
            name='date_creation',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Created'),
        ),
        migrations.AlterField(
            model_name='personnecentredinteret',
            name='date_last_modif',
            field=models.DateTimeField(auto_now=True, verbose_name='Last changed'),
        ),
        migrations.AlterField(
            model_name='personnediplome',
            name='date_creation',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Created'),
        ),
        migrations.AlterField(
            model_name='personnediplome',
            name='date_last_modif',
            field=models.DateTimeField(auto_now=True, verbose_name='Last changed'),
        ),
        migrations.AlterField(
            model_name='personnehobby',
            name='date_creation',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Created'),
        ),
        migrations.AlterField(
            model_name='personnehobby',
            name='date_last_modif',
            field=models.DateTimeField(auto_now=True, verbose_name='Last changed'),
        ),
        migrations.AlterField(
            model_name='personnelangue',
            name='date_creation',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Created'),
        ),
        migrations.AlterField(
            model_name='personnelangue',
            name='date_last_modif',
            field=models.DateTimeField(auto_now=True, verbose_name='Last changed'),
        ),
        migrations.AlterField(
            model_name='personnephoto',
            name='date_creation',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Created'),
        ),
        migrations.AlterField(
            model_name='personnephoto',
            name='date_last_modif',
            field=models.DateTimeField(auto_now=True, verbose_name='Last changed'),
        ),
        migrations.AlterField(
            model_name='personnetypepermis',
            name='date_creation',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Created'),
        ),
        migrations.AlterField(
            model_name='personnetypepermis',
            name='date_last_modif',
            field=models.DateTimeField(auto_now=True, verbose_name='Last changed'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='date_creation',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Created'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='date_last_modif',
            field=models.DateTimeField(auto_now=True, verbose_name='Last changed'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='date_creation',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Created'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='date_last_modif',
            field=models.DateTimeField(auto_now=True, verbose_name='Last changed'),
        ),
        migrations.AlterField(
            model_name='tagwithvalue',
            name='date_creation',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Created'),
        ),
        migrations.AlterField(
            model_name='tagwithvalue',
            name='date_last_modif',
            field=models.DateTimeField(auto_now=True, verbose_name='Last changed'),
        ),
        migrations.AlterField(
            model_name='texte',
            name='date_creation',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Created'),
        ),
        migrations.AlterField(
            model_name='texte',
            name='date_last_modif',
            field=models.DateTimeField(auto_now=True, verbose_name='Last changed'),
        ),
    ]
