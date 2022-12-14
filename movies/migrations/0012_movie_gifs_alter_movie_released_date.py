# Generated by Django 4.1.1 on 2022-11-28 05:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0011_alter_movie_released_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='gifs',
            field=models.ImageField(blank=True, null=True, upload_to='gifs/'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='released_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 11, 28, 5, 10, 13, 581543), null=True),
        ),
    ]
