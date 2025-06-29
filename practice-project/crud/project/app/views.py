from django.shortcuts import render,redirect
from .models import Student
# Create your views here.



def dashboard(request):
    data=Student.objects.all()
    return render(request,'dashboard.html',{'data':data})