from django.db import models
from django.db.models.fields import DateTimeField


# Create your models here.

class Albums(models.Model):
    title = models.CharField(max_length=250)
    artist = models.CharField(max_length=250, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    photo = models.CharField(max_length=250, null=True, blank=True)
    release_year = models.IntegerField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.title}, {self.artist}, {self.release_year}"
class Tracks(models.Model):
    name = models.CharField(max_length=250)
    albums = models.ForeignKey(
        Albums, 
        on_delete=models.CASCADE,
        related_name='tracks'
    )

