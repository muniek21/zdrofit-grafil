from django.db import models
from django.utils import timezone
import datetime


# Create your models here.

class ZdrofitClub(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    url = models.CharField(max_length=500)

    def __str__(self):
        return self.name


class Class(models.Model):
    day = models.CharField(max_length=20)
    hour = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    place = models.ForeignKey(ZdrofitClub, on_delete=models.CASCADE)
    date = models.DateTimeField('class_date')

    def __str__(self):
        return self.name

    def is_active(self):
        return self.date >= timezone.now()

    def stringify_class(self):
        return '{} {}'.format(self.name, self.date)
