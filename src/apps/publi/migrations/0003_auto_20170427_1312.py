# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-04-27 19:12
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('publi', '0002_auto_20170427_1308'),
    ]

    operations = [
        migrations.RenameField(
            model_name='publicacion',
            old_name='title',
            new_name='titulo',
        ),
    ]