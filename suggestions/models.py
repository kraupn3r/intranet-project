from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from accounts.choices.choices import *
from django.urls import reverse


class BoardCategory(models.Model):
    title = models.TextField(max_length=25)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('suggestions:category', args=[str(self.id)])

    class Meta:
        verbose_name_plural = "board categories"

class Post(models.Model):
    body = models.TextField(max_length=500)
    date_created = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey('auth.User', on_delete=models.PROTECT)
    title = models.CharField(max_length=200)

    category = models.ForeignKey(
        'suggestions.BoardCategory',
        on_delete=models.PROTECT,
        related_name="posts")

    last_activity = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('suggestions:postdetail', args=[str(self.id)])

    class Meta:
        ordering = ['-last_activity','-id']


class Comment(models.Model):
    Post = models.ForeignKey(
        'suggestions.Post', on_delete=models.CASCADE, related_name="comments")
    body = models.TextField(max_length=500)
    date_created = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey('auth.User', on_delete=models.PROTECT)

    def __str__(self):
        return self.body[0:20]

    def save(self, *args, **kwargs):
        self.Post.last_activity = timezone.now()
        self.Post.save()
        super(Comment, self).save(*args, **kwargs)
