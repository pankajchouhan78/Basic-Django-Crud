from django.db import models


# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=50)
    collage = models.CharField(max_length=100,default="mit")
    year = models.IntegerField(default=2020)
    stream = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class CAR(models.Model):
    car_name = models.CharField(max_length=50)
    speed = models.IntegerField(default=50)
    def __str__(self):
        return self.car_name