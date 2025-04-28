from django.db import models

# Create your models here.

class UserApp(models.Model):
    user_username=models.CharField(max_length=50)