from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    collection = models.CharField(max_length=255, default='-')
    type = models.CharField(max_length=255, default="-")
    year = models.IntegerField(default=0)
    amount = models.IntegerField(default=0)
    description = models.TextField()