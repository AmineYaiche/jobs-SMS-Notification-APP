# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import app.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('phone_number', models.CharField(max_length=12, )),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='job',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=30)),
                ('professions', models.CharField(max_length=30)),
                ('recruiter', models.CharField(max_length=30)),
                ('link', models.URLField()),
                ('education_level', models.CharField(max_length=30)),
                ('regin', models.CharField(max_length=30)),
                ('publication_date', models.CharField(max_length=30)),
                ('experience_level', models.CharField(max_length=30)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
