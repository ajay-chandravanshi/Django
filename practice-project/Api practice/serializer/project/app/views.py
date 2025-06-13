from django.shortcuts import render
from django.http import JsonResponse
from models import Student
from serializer import StudentSerializer

# Create your views here.

def student_list(request):
    stu=Student.objects.all()
    print(stu)
    print(type(stu))
    