from django.db import models

# Create your models here.
class  Product(models.Model):
    title = models.CharField()
    author = models.CharField()
    category = models.CharField()
    synopsis = models.TextField()
    price = models.IntegerField()
    rating = models.IntegerField()
    year = models.IntegerField()
    pages = models.IntegerField()

    # Models blum di migrate karena blm fix