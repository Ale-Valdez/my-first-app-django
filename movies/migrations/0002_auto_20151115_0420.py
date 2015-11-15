# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pelicula',
            name='anio',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='pelicula',
            name='vista',
            field=models.BooleanField(default=False),
        ),
    ]
