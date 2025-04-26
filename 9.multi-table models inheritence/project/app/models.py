from django.db import models

# Create your models here.

class BaseInfo(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(unique=True)
    contact=models.IntegerField()
class Student(BaseInfo):
    branch=models.CharField(max_length=50)
    fees=models.IntegerField()
class Employee(BaseInfo):
    Deparment=models.CharField(max_length=50)
    Salary=models.IntegerField()
    