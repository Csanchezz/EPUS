# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-04-19 16:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('escuela', '0006_escuela_mapa'),
        ('tpe', '0013_auto_20170417_1629'),
    ]

    operations = [
        migrations.CreateModel(
            name='EquipamientoOs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sistema_operativo', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='equipamiento',
            name='fotos_link',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='equipamiento',
            name='poblacion',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='escuela.EscPoblacion'),
        ),
        migrations.AddField(
            model_name='ticketreparacionrepuesto',
            name='fecha_autorizado',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='ticketreparacionrepuesto',
            name='fecha_solicitud',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='ticketreparacionrepuesto',
            name='autorizado',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='equipamiento',
            name='equipo_os',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tpe.EquipamientoOs'),
        ),
        migrations.AddField(
            model_name='equipamiento',
            name='servidor_os',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='servidores', to='tpe.EquipamientoOs'),
        ),
    ]