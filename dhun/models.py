from django.db import models
from django.db.models.deletion import CASCADE
from django.urls import reverse
# Create your models here.

class User(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField()
    username=models.CharField(max_length=30,unique=True)
    password=models.CharField(max_length=30)

    def __str__(self):
        return f'username:{self.username}'

class Album(models.Model):
    userid=models.ForeignKey(User,on_delete=models.CASCADE)
    album_name=models.CharField(max_length=50)
    artist_name=models.CharField(max_length=50)
    album_logo=models.FileField()
    album_genre=models.CharField(max_length=50)

    def __str__(self):
        return f'album_name:{self.album_name}'
    def get_absolute_url(self):
        return reverse("dhun:home")

class Song(models.Model):
    album_id=models.ForeignKey(Album,on_delete=models.CASCADE)
    song_name=models.CharField(max_length=50)
    song_image=models.FileField()
    song=models.FileField()

    def __str__(self):
        return f'song_name:{self.song_name}, album_id:{self.album_id}'
    
    def get_absolute_url(self):
        return reverse("dhun:home")
    
# class Playlist(models.Model):
    
# class Recent(models.Model):
    
# class Favourite(models.Model):
    
