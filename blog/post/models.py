from django.db import models
from django.conf import settings
from django.utils import timezone


class Blog(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    count = models.IntegerField()

    def __str__(self):
        return self.title

class Comment(models.Model):
 
    post = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments')
    date = models.DateTimeField(default=timezone.now)
    author = models.CharField(max_length=20)
    text = models.TextField()
    count = models.IntegerField()

    def __str__(self):
        return self.text