from django.db import models

# Create your models here.

class Album(models.Model):
    album_title = models.CharField(max_length=455)
    artist = models.CharField(max_length=455)
    created_at = models.DateTimeField(auto_now_add=True)