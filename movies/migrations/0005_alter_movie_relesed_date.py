# Generated by Django 4.1.1 on 2022-11-16 01:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0004_movie_info_movie_relesed_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='relesed_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 11, 16, 1, 16, 58, 857141)),
        ),
    ]