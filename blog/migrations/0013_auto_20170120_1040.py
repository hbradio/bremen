# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-20 15:40
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_auto_20170120_0952'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='content',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='post',
            name='abstract',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=ckeditor.fields.RichTextField(),
        ),
    ]