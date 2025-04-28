from django.shortcuts import render
from .models import Client
# Create your views here.

def home(request):
    return render(request,'home.html')
def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html')
def gallery(request):
    return render(request,'gallery.html')
def services(request):
    return render(request,'services.html')
def book_event(request):
    return render(request,'book_event.html')
def book_room(request):
    return render(request,'book_room.html')
def login(request):
    return render(request,'login.html')
def logindata(request):

    return render(request,'logindata.html')
def register(request):
    return render(request,'register.html')

def registerdata(request):
    print(request.method)
    print(request.POST)

    username=request.POST.get('username')
    email=request.POST.get('email')
    phone=request.POST.get('phone')
    dob=request.POST.get('dob')
    gender=request.POST.get('gender')
    image=request.FILES.get('profile-pic')
    detail=request.POST.get('detail')
    password=request.POST.get('password')
    cpassword=request.POST.get('cpassword')
    print(username,email,phone,dob,gender,image,detail,password,cpassword)

    data=Client.objects.filter(clt_email=email)

    if data:
        msg = "Email already registered. Please log in"
        return render(request, 'register.html', {'msg': msg, 'msg_type': 'email_error'})
    
    else:
        if password==cpassword:
            msg = "Registered Successfully!"
            return render(request, 'login.html', {'msg': msg, 'msg_type': 'success'})
        
        else:
            msg="Password and Confirm password not match"
            userdata={'username':username,'email':email,'phone':phone,'detail':detail}
            return render(request,'register.html',{'msg':msg,'msg_type': 'password_mismatch','data':userdata})