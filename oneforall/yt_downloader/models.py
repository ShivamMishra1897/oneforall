from django.db import models

# Create your models here.

class Video(models.Model):
    title = models.CharField(max_length=150)
    url_link = models.URLField()

    def __str__(self):
        return self.title
    
    