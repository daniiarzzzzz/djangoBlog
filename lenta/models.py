from django.db import models

# Create your models here.


class Post(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=150)
    description = models.TextField()
    like = models.IntegerField(default=0)
