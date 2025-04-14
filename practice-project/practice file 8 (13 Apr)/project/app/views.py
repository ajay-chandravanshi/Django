from django.shortcuts import render

# Create your views here.

def landing(request):
    return render(request,'home.html')

def home(request):
    data={'name':'Ajay','age':23,'quali':'Btech'}
    return render(request,'home.html',{'data':data})