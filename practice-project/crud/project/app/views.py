from django.shortcuts import render,redirect
from .models import Student
# Create your views here.

def register(request):
    if request.method=='POST':
        uname=request.POST.get('name')
        uemail=request.POST.get('email')
        ucity=request.POST.get('city')
        Student.objects.create(name=uname,email=uemail,city=ucity)
        return redirect('dashboard')
    return render(request,'register.html')

def dashboard(request):
    data=Student.objects.all()
    return render(request,'dashboard.html',{'data':data})