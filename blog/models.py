from django.db import models
from django.urls import reverse
from . import forms

# Create your models here.
class auth_User(models.Model):
    username = forms.User
    password = forms.User

class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    body = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])
