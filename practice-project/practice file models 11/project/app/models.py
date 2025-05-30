from django.db import models

# Create your models here.

class student(models.Model):
    stu_name=models.CharField(max_length=50)
    stu_email=models.EmailField(unique=True)
    stu_dis=models.CharField(max_length=200)
    stu_contact=models.IntegerField()
    stu_dob=models.DateField()
    stu_quali=models.CharField(max_length=50)
    stu_gender=models.CharField(max_length=50)
    stu_image=models.ImageField(upload_to='image/')
    stu_document=models.FileField(upload_to='file/')
    stu_password=models.CharField(max_length=15)

class UserProfile(models.Model):
    quail=[("1",'bba'),("2",'mba')]

    username=models.CharField(max_length=30, null=True,unique=True,db_index=True,blank=False,help_text="enter a username")

    email=models.EmailField(max_length=255, unique=True,blank=False,db_index=True)

    bio=models.CharField(max_length=50,blank=True,null=True,db_index=True,help_text="write a short bio about your")

    is_active= models.BooleanField(default=False,db_index=True)

    Qualification=models.CharField(max_length=100,choices=quail,null=True,  verbose_name='Quali',db_index=True)
def str(self):
  return self.emailt+" "+self.username+""