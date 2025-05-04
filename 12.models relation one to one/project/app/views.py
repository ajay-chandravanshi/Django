from django.shortcuts import render
from .models import Student
# Create your views here.

def User(request):
    data=Student.objects.all()
    print(data)
    print(data.values())
    print(data.values_list())

    data1=Student.objects.get(name='ajay')
    print(data1.name)
    print(data1.email)
    print(data1.contact)
    print(data1.roll)
    print(data1.aadhar)
    print(data1.aadhar.adharno)
    print(data1.aadhar.crteatedby)