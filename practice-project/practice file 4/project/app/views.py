from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
# Create your views here.

def home(request):
    x="<h1>Hello sir<h1/>"
    y="<h2>This is ajay chandravanshi</h2>"
    return HttpResponse(x+y)

def json(request):
    data={'name':True,'age':False,'student':None,'n':'ajay'}
    return JsonResponse(data)

def link(request):
    return redirect('https://www.google.com')

def new(request):
    # x={}
    # z=[{'name':'Ajay','age':24,'degree':'B.tech'},{'name':'Aniket','age':21,'degree':'parmacy'}]
    # x['key1']=z
    # print(x)
    # return render(request,'index.html',{'key1':z})
    
    # data={'name':'Ajay','age':24,'degree':'B.tech'}
    # return render(request,'index.html',data)
   