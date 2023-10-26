from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.TextField(null=True, blank=True)
    authors = models.TextField(null=True, blank=True)
    categories = models.TextField(null=True, blank=True)
    thumbnail = models.URLField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    published_year = models.IntegerField(null=True, blank=True)
    average_rating = models.FloatField(null=True, blank=True)
    num_pages = models.IntegerField(null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)