from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserMenu(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    title = models.TextField(null=True, blank=True)
    authors = models.TextField(null=True, blank=True)
    categories = models.TextField(null=True, blank=True)
    thumbnail = models.URLField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    published_year = models.IntegerField(null=True, blank=True)
    average_rating = models.FloatField(null=True, blank=True)
    num_pages = models.IntegerField(null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)

class User(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)