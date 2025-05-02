from django.db import models

# Create your models here.

class Aadhar(models.Model):
    adharno=models.IntegerField(unique=True)
    crteatedby=models.CharField(max_length=40)

    def __str__(self):
        return str(self.adharno)

class Student(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(unique=True)
    contact=models.IntegerField()
    roll=models.IntegerField()
    aadhar=models.OneToOneField(Aadhar,on_delete=models.PROTECT,to_field="adharno")

    def __str__(self):
        return self.name
