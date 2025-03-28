from django.db import models

class Product(models.Model):
    Name = models.CharField(max_length=100)
    price = models.DecimalField()
    