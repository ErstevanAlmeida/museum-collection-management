from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    collection = models.CharField(max_length=255, default='-')
    type = models.CharField(max_length=255, default="-")
    year = models.IntegerField(default=0)
    amount = models.IntegerField(default=0)
    description = models.TextField()