from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse

# Create your views here.

def home(request):
    x="<h1>Hello sir ji<h1/>"
    return HttpResponse(x)

def jsonfile(request):
    data={'name':True,'age':False,'year':None}
    return JsonResponse(data)

def renderfile(request):
    return redirect('https://www.google.com')

def htmlfile(request):
    return render(request,'index.html')