from django.contrib import admin
from .models import Student
# Register your models here.

# admin.site.register(Student)

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display=['id','stu_name','stu_email','stu_contact','stu_city']