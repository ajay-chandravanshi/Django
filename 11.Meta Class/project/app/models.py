from django.db import models

# Create your models here.

class Student(models.Model):
    stu_name=models.CharField(max_length=100)
    stu_email=models.EmailField(unique=True)
    stu_contact=models.IntegerField()
    stu_city=models.CharField(max_length=100)

    class Meta: # kissi bhi class ke internal behaviour ko change karne ke liye meta class use karte hai
        db_table='Student' # db squlite mai table data ka name change hota hai
        verbose_name='NewName' # admin panel pai table ka name change karne ke liye
        verbose_name_plural='Student' # admin panel pai table ke name mai se s hatane ke liye
        # ordering=['id'] # ascending order mai lane ke liye
        # ordering=['-id'] # descending order mai lane ke liye
        # ordering=['stu_name'] # name ke hisab se order mai jam jayega