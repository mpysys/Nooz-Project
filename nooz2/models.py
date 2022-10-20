from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=255)
    title_tag = models.CharField(max_length=255)
    description = models.CharField(max_length=50, default='Click above to read more')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    timestamp = models.DateField(auto_now_add=True)
    category = models.CharField(max_length=255, default='News')

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        return reverse('home')


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home')
