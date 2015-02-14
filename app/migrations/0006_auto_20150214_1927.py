# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import app.models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20150209_1318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='phone_number',
            field=models.CharField(max_length=12, validators=[app.models.validate_number]),
            preserve_default=True,
        ),
    ]
