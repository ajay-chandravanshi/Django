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
    # return render(request,'index.html')

    # first type below code 
    # data=[{'name':'Ajay','city':'Bhopal'},{'name':'Animesh','city':'Indore'}]
    # return render(request,'index.html',{'key1':data})

    # second type above code 
    # x={}
    # data=[{'name':'Ajay','city':'Bhopal'},{'name':'Animesh','city':'Indore'}]
    # x['key1']=data
    # return render(request,'index.html',x)

    # code for single data 
    # new={'name':'Ajay','city':'Bhopal'}
    # return render(request,'index.html',new)

    # above code access all value 
    y={}
    new={'name':'Ajay','city':'Bhopal'}
    y['key1']=new
    return render(request,'index.html',y)

def new(request):
    return redirect('https://www.google.com')

