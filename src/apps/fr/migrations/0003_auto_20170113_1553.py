# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-01-13 15:53
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fr', '0002_auto_20161115_1406'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='etiqueta',
            options={'ordering': ('etiqueta',), 'verbose_name': 'Etiqueta', 'verbose_name_plural': 'Etiquetas'},
        ),
        migrations.AlterModelOptions(
            name='evento',
            options={'ordering': ('nombre',), 'verbose_name': 'Evento', 'verbose_name_plural': 'Eventos'},
        ),
    ]