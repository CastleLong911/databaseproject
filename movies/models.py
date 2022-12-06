from django.db import models
import datetime

class Movie(models.Model):
    title = models.CharField(max_length=200, blank=False, null=False)
    ratio = models.FloatField(default=0.0, blank=False,null=False)
    intro = models.CharField(max_length=1000, blank=True, null=True)
    thumbnail = models.ImageField(upload_to='images/', blank=False, null=False)
    gifs = models.ImageField(upload_to='gifs/', blank=True, null=True)
    info = models.CharField(max_length=200, blank=False, null=False, default='None')
    released_date = models.DateTimeField(blank=True, null=True, default=datetime.datetime.now())

class Review(models.Model):
    movieId = models.ForeignKey('Movie', related_name='movieid', on_delete=models.CASCADE, db_column='movieId')
    userId = models.ForeignKey('auth.User', related_name='userid', on_delete=models.CASCADE, db_column='userId')
    ratio = models.IntegerField(blank=False, null=False)
    reviewText = models.CharField(max_length=200, blank=False, null=False)
    created_at = models.DateTimeField(default=datetime.datetime.now)

