# Generated by Django 4.1.1 on 2022-10-17 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_alter_movie_thumbnail'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='intro',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]