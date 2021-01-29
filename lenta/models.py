from django.db import models

# Create your models here.


class Post(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.CharField('Post title', max_length=150)
    description = models.TextField()
    like = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    text = models.CharField('comment text', max_length=200)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text
