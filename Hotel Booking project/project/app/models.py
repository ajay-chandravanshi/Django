from django.db import models

# Create your models here.

class Student(models.Model):
    stu_username=models.CharField(max_length=50)
    stu_email=models.EmailField(unique=True)
    stu_phone=models.IntegerField()
    stu_dob=models.DateField()
    stu_gender=models.CharField(max_length=10)
    stu_image=models.ImageField(upload_to='image/')
    stu_detail=models.CharField(max_length=100)
    stu_password=models.CharField(max_length=20)
    stu_cpassword=models.CharField(max_length=20)