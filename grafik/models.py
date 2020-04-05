from django.db import models


# Create your models here.

class ZdrofitClub(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)


class Class(models.Model):
    day = models.CharField(max_length=20)
    hour = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    place = models.ForeignKey(ZdrofitClub, on_delete=models.CASCADE)
    date = models.DateTimeField('class_date')
