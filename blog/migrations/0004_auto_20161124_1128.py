# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2016-11-24 16:28
from __future__ import unicode_literals

from django.db import migrations
import froala_editor.fields
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
        ('blog', '0003_auto_20161123_1130'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='content',
            field=froala_editor.fields.FroalaField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]