# Generated by Django 4.1.1 on 2022-11-16 01:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0006_remove_movie_relesed_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='relesed_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 11, 16, 1, 18, 20, 965695)),
        ),
    ]