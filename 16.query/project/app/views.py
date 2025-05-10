from django.shortcuts import render
from .models import Student
# Create your views here.

def home(request):
    # filter code below
    data=Student.objects.filter(name="ajay")
    print(data)
    print(data.values())
    print(data.values_list())

    # data=Student.objects.filter(name="ajay",email="ajay@gmail.com")
    # print(data)
    # print(data.values())
    # print(data.values_list())

    # all query below
    # all_data=Student.objects.all()
    # print(all_data)
    # print(all_data.values())
    # print(all_data.values_list())



def index(request):
    return render(request,'index.html')
def first(request):
    x=Student.objects.first()
    return render(request,'index.html',{'data':x})