from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
# Create your views here.

def home(request):
    x="<h1>This is home page,do you like it<h1/>"
    return HttpResponse(x)

def index(request):
    return render(request,'index.html')

def json(request):
    data={'name':True,'age':False,'student':None,'n':'ajju','y':'asshajs'}
    return JsonResponse(data)

def new(request):
    return redirect("https://www.google.com")
