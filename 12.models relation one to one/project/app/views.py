from django.shortcuts import render
from .models import Student
# Create your views here.

def User(request):
    data=Student.objects.all()
    print(data)
    print(data.values())
    print(data.values_list())
