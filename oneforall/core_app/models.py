from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    username = models.CharField(max_length=75,unique=True,blank=False)
    email = models.EmailField(max_length=75,unique=True)

    def __str__(self):
        return self.username

# class UserProfile(models.Model):
#     user = models.OneToOneField(on_delete=models.CASCADE)
