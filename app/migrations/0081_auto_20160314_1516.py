# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
import django_markdown.models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0080_personne_reset_password'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_creation', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('date_last_modif', models.DateTimeField(auto_now=True, verbose_name='Last changed')),
                ('date_v_debut', models.DateTimeField(default=django.utils.timezone.now, verbose_name='V. start')),
                ('date_v_fin', models.DateTimeField(default=None, null=True, verbose_name='V. end', blank=True)),
                ('label', models.CharField(default=None, max_length=200, blank=True, help_text='A recall of what this blog contains, language independant)', null=True, verbose_name='Label')),
                ('date_publication', models.DateTimeField(default=datetime.datetime.now, null=True, verbose_name='Publication date', blank=True)),
                ('ordre_si_top', models.IntegerField(default=None, help_text='Priority: the lowest the higher ("1" is <b>before</b> "2" and so on...).<br /><b>Let it blank if you don\'t want this blog on top</b>', null=True, verbose_name='If this blog is always on top', blank=True)),
            ],
            options={
                'ordering': ['date_v_debut'],
                'abstract': False,
                'verbose_name': 'Blog',
                'verbose_name_plural': 'Blogs',
            },
        ),
        migrations.CreateModel(
            name='BlogTraduit',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_creation', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('date_last_modif', models.DateTimeField(auto_now=True, verbose_name='Last changed')),
                ('date_v_debut', models.DateTimeField(default=django.utils.timezone.now, verbose_name='V. start')),
                ('date_v_fin', models.DateTimeField(default=None, null=True, verbose_name='V. end', blank=True)),
                ('locale', models.CharField(default=None, max_length=2, blank=True, help_text="Blog's locale (en, fr, ...)", null=True, verbose_name="Blog's locale")),
                ('title', models.CharField(default=None, max_length=200, blank=True, help_text="Blog's title", null=True, verbose_name='Title')),
                ('content', django_markdown.models.MarkdownField(default=None, help_text="Blog's content", null=True, verbose_name='Content', blank=True)),
                ('blog', models.ForeignKey(default=None, blank=True, to='app.Blog', null=True)),
            ],
            options={
                'ordering': ['date_v_debut'],
                'abstract': False,
                'verbose_name': 'Blog-translated content',
                'verbose_name_plural': 'Blogs-translated',
            },
        ),
        migrations.AlterModelOptions(
            name='activite',
            options={'ordering': ['-date_publication', '-date_last_modif']},
        ),
        migrations.AddField(
            model_name='activite',
            name='date_publication',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Created'),
        ),
        migrations.AlterField(
            model_name='activite',
            name='activite',
            field=models.IntegerField(default=0, choices=[(0, 'has a new relationship:'), (1, 'has a new travel:'), (2, "has changed a travel, it's now:"), (3, "Cogofly's news")]),
        ),
        migrations.AddField(
            model_name='activite',
            name='blog_traduit',
            field=models.ForeignKey(default=None, to='app.BlogTraduit', blank=True, help_text='Blog translated', null=True, verbose_name='Blog translated'),
        ),
    ]
