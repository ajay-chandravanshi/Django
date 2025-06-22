from django.db import models



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



class Query(models.Model):
    stu_name=models.CharField(max_length=50)
    stu_email=models.EmailField()
    stu_query=models.CharField(max_length=150)


class Room(models.Model):
    room_image=models.ImageField(upload_to='image/')
    room_name=models.CharField(max_length=30)
    room_price=models.IntegerField()
    room_size=models.IntegerField()
    room_capacity=models.IntegerField()
    room_bed=models.CharField(max_length=25)
    room_services=models.CharField(max_length=30)
