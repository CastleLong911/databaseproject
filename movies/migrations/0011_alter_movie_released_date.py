# Generated by Django 4.1.1 on 2022-11-16 01:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0010_alter_movie_released_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='released_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 11, 16, 1, 26, 18, 189714), null=True),
        ),
    ]