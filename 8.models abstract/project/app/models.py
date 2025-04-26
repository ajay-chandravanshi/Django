from django.db import models
# Create your models here.

class BaseInfo(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField(max_length=255)
    contact=models.IntegerField()
    class Meta:
        abstract=True
    
class Student(BaseInfo):
    branch=models.CharField(max_length=15)
    
class Employee(BaseInfo):
    department=models.CharField(max_length=15)
    salary=models.IntegerField()
    
class Client(BaseInfo):
    project=models.CharField(max_length=15)

class User(BaseInfo):
    User_id=models.IntegerField()

    def __str__(self):
        return self.name
