# model.py
from django.db import models

class Movie(models.Model):
    name = models.CharField(max_length=20)
    imdb = models.IntegerField()
    ticket = models.IntegerField()
    actor = models.CharField(max_length=20)
    director = models.CharField(max_length=20)
    release = models.DateTimeField()