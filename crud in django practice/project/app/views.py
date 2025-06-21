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

def edit(request,id):
    student=Student.objects.get(id=id)
    return render(request,'edit.html',{'student':student})

def update(request,id):
    if request.method=='POST':
        student=Student.objects.get(id=id)
        student.name=request.POST.get('name')
        student.email=request.POST.get('email')
        student.city=request.POST.get('city')
        student.save()
        return redirect('dashboard')
    
def delete(request,id):
    student=Student.objects.get(id=id)
    student.delete()
    return redirect('dashboard')   
   