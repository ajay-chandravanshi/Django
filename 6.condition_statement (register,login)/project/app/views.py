from django.shortcuts import render

# Create your views here.
def landing(request):
    data={'name':'Ajay','age':23,'quali':'btech'}
    return render(request,'home.html',{'data':data})
def home(request):
    return render(request,'home.html')
def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html')
def login(request):
    return render(request,'login.html')
def register(request):
    return render(request,'register.html')
def registerdata(request):
    print(request.method)
    print(request.POST)

    username=request.method.GET('username')
    email=request.method.POST('email')
    detail=request.method.POST('detail')
    phone=request.method.POST('phone')
    dob=request.method.POST('dob')
    subscribe=request.method.GETlist('subscribe')
    gender=request.method.POST('gender')
    password=request.method.POST('password')
    cpassword=request.method.POST('cpassword')
    print(username,email,detail,phone,dob,subscribe,gender,password,cpassword)