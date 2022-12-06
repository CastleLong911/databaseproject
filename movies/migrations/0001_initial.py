# Generated by Django 4.1.1 on 2022-10-17 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('ratio', models.FloatField(default=0.0)),
                ('thumbnail', models.ImageField(upload_to='static/images/')),
            ],
        ),
    ]
