from django.db import models

# Create your models here.

class student(models.Model):
    stu_name=models.CharField(max_length=50)
    stu_email=models.EmailField(unique=True)
    stu_detail=models.CharField(max_length=50)
    stu_phone=models.IntegerField()
    stu_dob=models.DateField()
    stu_subscribe=models.CharField(max_length=20)
    stu_gender=models.CharField(max_length=10)
    stu_image=models.ImageField(upload_to='image/')
    stu_document=models.FileField(upload_to='File/')
    stu_password=models.CharField(max_length=15)
