from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class User(models.Model):
  username = models.CharField(max_length=50,primary_key=True)
  email = models.EmailField()
  password = models.CharField(max_length=50)
# Create your models here.
class Song(models.Model):
    movie = models.CharField(max_length=255, default='SOME STRING')
    title = models.CharField(max_length=255)
    artist = models.CharField(max_length=255, blank=True)
    song_file = models.FileField(upload_to='music')
    image_url = models.CharField(max_length=500, default='SOME STRING')

class WatchLater(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    song = models.ForeignKey(Song, on_delete=models.CASCADE)