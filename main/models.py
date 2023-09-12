from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    collection = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    year = models.IntegerField()
    amount = models.IntegerField()
    description = models.TextField()