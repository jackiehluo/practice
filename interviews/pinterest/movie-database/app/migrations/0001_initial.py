# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('title', models.TextField()),
                ('year', models.TextField()),
                ('genre', models.TextField()),
            ],
            options={
                'db_table': 'movies',
                'managed': True,
            },
            bases=(models.Model,),
        ),
    ]
