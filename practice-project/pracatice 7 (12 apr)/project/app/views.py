from django.shortcuts import render

# Create your views here.

def home(request):
    x={'name':'Ajay','age':23,'quali':'btech'}
    first=[1,2,3]
    second=[4,5,6]
    y={}
    
    data=[
    {"name": "zed", "age": 19},
    {"name": "amy", "age": 22},
    {"name": "joe", "age": 31},
    ]

    y['key1']=data
    return render(request,'home.html',y)




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

    username=request.POST.get('username')
    email=request.POST.get('email')
    detail=request.POST.get('detail')
    phone=request.POST.get('phone')
    dob=request.POST.get('dob')
    subscribe=request.POST.getlist('subscribe')
    gender=request.POST.get('gender')
    password=request.POST.get('password')
    cpassword=request.POST.get('cpassword')
    print(username,email,detail,phone,dob,subscribe,gender,password,cpassword)