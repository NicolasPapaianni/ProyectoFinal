from django.db import models



class Products(models.Model):
    name = models.CharField(max_length=60)
    price = models.FloatField()
    description = models.CharField(max_length=300, null=True, blank=True)
    stock = models.IntegerField()
    is_active = models.BooleanField(default=True)


class Category(models.Model):
    name = models.CharField(max_length=100)

