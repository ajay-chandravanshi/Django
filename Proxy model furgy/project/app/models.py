from django.db import models

# Create your models here.

class MainModel(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(unique=True)
    contact=models.IntegerField()
    department=models.CharField(max_length=50)
    employeeid=models.IntegerField()
    address=models.CharField(max_length=50)

class ProxyModel(MainModel):
    class Meta:
        proxy=True    