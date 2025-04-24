from django.contrib import admin
from .models import BaseInfo,Student,Employee
# Register your models here.

admin.site.register(Student)
admin.site.register(Employee)
admin.site.register(BaseInfo)