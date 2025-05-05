from django.shortcuts import render
from .models import Student,Department
# Create your views here.

def student(request):
    data=Student.objects.all()
    print(data)
    print(data.values())
    print(data.values_list)

    stu_data=Student.objects.get(stu_name="ajay")
    print(stu_data.id)
    print(stu_data.stu_name)
    print(stu_data.stu_email)

    x=stu_data.stu_dep
    print(x.dep_name)
    print(x.dep_des)
    print(x.dep_hod)

def department(request):
    data=Department.objects.all()
    print(data)
    print(data.values())
    print(data.values_list)

    dep_data=Department.objects.get(id=1)
    print(dep_data.id)
    print(dep_data.dep_name)
    print(dep_data.dep_des)
    print(dep_data.dep_hod)

    print((dep_data.depart.all()).count())
    
    x=dep_data.depart.all()
    for i in x:
        print(i.stu_name)
        print(i.stu_email)
