from django.db import models


# Create your models here.
# name,writer,price,discount---writer and book CRUD

class Writer(models.Model):
    name = models.CharField(max_length=255)


class Book(models.Model):
    name = models.CharField(max_length=255)
    writer = models.ForeignKey(Writer, on_delete=models.CASCADE)
    price = models.FloatField()
    discount = models.FloatField()
