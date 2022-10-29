from django.db import models

# Create your models here.
class Artiste(models.Model):
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 30)
    age = models.IntegerField()

class Song(models.Model):
    title = models.CharField(max_length = 100)
    date_released = models.DateField()
    likes = models.IntegerField()
    artiste_id = models.ForeignKey(Artiste, on_delete = models.CASCADE)

class Lyric(models.Model):
    content = models.CharField(max_length = 200)
    song_id = models.ForeignKey(Song, on_delete = models.CASCADE)