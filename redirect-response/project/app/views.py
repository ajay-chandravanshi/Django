from django.shortcuts import render,redirect
from django.http import HttpResponse
# Create your views here.

def home(request):
    # return redirect("https://www.google.com")
    name,city='ajay','Bhopal'
    return redirect(f"/index/?name={name}&city={city}")

def index(request):
    print(request.method)
    print(request.GET)
    x=request.GET.get('name')
    y=request.GET.get('city')
    return render(request,'index.html',{'key1':x,'key2':y})
    

