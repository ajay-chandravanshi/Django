from django.db import models
# Create your models here.

class Fuel(models.Model):
    Fuel_name=models.CharField(unique=True,max_length=50)
    def __str__(self):
        return self.Fuel_name

class Vehicles(models.Model):
    Vehicle_name=models.CharField(max_length=50)
    Fuel_name = models.ManyToManyField(Fuel,related_name='vehical')

    def __str__(self):
        return self.Vehicle_name

class Student(models.Model):
    stu_name= models.CharField(max_length=50)