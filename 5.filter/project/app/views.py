from django.shortcuts import render

# Create your views here.

def home(request):
    x={'name':'ajay','age':23,'quali':'BTECH'}
    return render(request,'home.html',x)
