from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse

# Create your views here.

def home(request):
    x="<h1>Hello sir what is your name</h1>"
    return HttpResponse(x)

def directfile(request):
    return render('https://www.google.com')

def jsonfile(request):
    data={'name':'ajay','roll':1212,'sub':'english'}
    return JsonResponse(data)

def renderfile(request):
    return render(request,'home.html')