# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_auto_20151115_0420'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dvd',
            name='descripcion',
            field=models.TextField(null=True, blank=True),
        ),
    ]
