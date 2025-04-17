from django.db import models

# Create your models here.

class student(models.Model):
    stu_name=models.CharField(max_length=50),
    stu_email=models.EmailField(),
    stu_detail=models.CharField(max_length=200),
    stu_phone=models.IntegerField(),
    stu_dob=models.DateField(),
    stu_subscribe=models.CharField(max_length=50),
    stu_gender=models.CharField(max_length=15),
    stu_image=models