# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-01-08 23:23
from __future__ import unicode_literals

from django.db import migrations, models
import djangocms_blog.fields


class Migration(migrations.Migration):

    dependencies = [
        ('djangocms_blog', '0031_auto_20170610_1744'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogcategorytranslation',
            name='meta_description',
            field=models.TextField(blank=True, default='', verbose_name='post meta description'),
        ),
        migrations.AlterField(
            model_name='blogcategorytranslation',
            name='name',
            field=models.CharField(max_length=2000, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='blogcategorytranslation',
            name='slug',
            field=models.SlugField(blank=True, max_length=2000, verbose_name='slug'),
        ),
        migrations.AlterField(
            model_name='posttranslation',
            name='meta_title',
            field=models.CharField(blank=True, default='', help_text='used in title tag and social sharing', max_length=2000, verbose_name='post meta title'),
        ),
        migrations.AlterField(
            model_name='posttranslation',
            name='slug',
            field=djangocms_blog.fields.AutoSlugField(allow_unicode=True, blank=True, db_index=False, max_length=2000, verbose_name='slug'),
        ),
        migrations.AlterField(
            model_name='posttranslation',
            name='title',
            field=models.CharField(max_length=2000, verbose_name='title'),
        ),
    ]
