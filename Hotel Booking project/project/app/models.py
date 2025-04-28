from django.db import models

# Create your models here.

class Client(models.Model):
    clt_username=models.CharField(max_length=50)
    clt_email=models.EmailField(unique=True)
    clt_phone=models.IntegerField()
    clt_dob=models.DateField()
    clt_gender=models.CharField(max_length=10)
    clt_image=models.ImageField(upload_to='image/')
    clt_detail=models.CharField(max_length=100)
    clt_password=models.CharField(max_length=20)
    clt_cpassword=models.CharField(max_length=20)