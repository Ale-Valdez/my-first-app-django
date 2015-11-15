# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100, blank=True)),
                ('nacionalidad', models.CharField(max_length=100, blank=True)),
                ('fecha_nac', models.DateField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Dvd',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('numero', models.IntegerField()),
                ('descripcion', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tipo', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Pelicula',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=200)),
                ('descripcion', models.TextField()),
                ('calidad', models.CharField(default=b'n-n', max_length=3, choices=[(b'n-n', b'NONE'), (b'dvd', b'DVD-RIP'), (b'cam', b'CAM-RIP'), (b'hd', b'HD')])),
                ('duracion', models.TimeField()),
                ('autores', models.ManyToManyField(to='movies.Actor')),
                ('dvd', models.ForeignKey(to='movies.Dvd')),
                ('generos', models.ManyToManyField(to='movies.Genero')),
            ],
        ),
    ]
