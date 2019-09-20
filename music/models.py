from django.db import models

# Create your models here.


class Album(models.Model):
	artist = models.CharField(max_length = 250)
	album_name = models.CharField(max_length = 250)
	genre = models.CharField(max_length = 250)

	def __str__(self):
		return self.artist + '' + self.album_name


class Song(models.Model):
	album = models.ForeignKey(Album, on_delete= models.CASCADE)
	song_name = models.CharField(max_length = 250)
	is_favorite = models.BooleanField(default= False)
	
	def __str__(self):
		return self.song_name




