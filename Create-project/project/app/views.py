from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse

# Create your views here.
def home(request):
    x="<h1 style='color:red'>Hello...</h1>"
    y="<div style='border:2px'>Hello sir..</div>"
    return HttpResponse(y)

def about(request):
    data={'name':True,'age':False,'qual':None}
    return JsonResponse(data)

def index(request):
    return render(request,'index.html')

def new(request):
    return redirect('https://www.google.com')

