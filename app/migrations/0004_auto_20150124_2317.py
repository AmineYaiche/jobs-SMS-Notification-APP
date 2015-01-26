# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20150124_2245'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='education_level',
        ),
        migrations.RemoveField(
            model_name='job',
            name='experience_level',
        ),
        migrations.RemoveField(
            model_name='job',
            name='professions',
        ),
        migrations.RemoveField(
            model_name='job',
            name='publication_date',
        ),
        migrations.RemoveField(
            model_name='job',
            name='region',
        ),
    ]
