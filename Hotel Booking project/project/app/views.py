from django.shortcuts import render
from .models import UserApp
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

    UserApp.objects.create(stu_username=username,stu_email=email,stu_phone=phone,stu_dob=dob,stu_gender=gender,stu_image=image,stu_detail=detail,stu_password=password,stu_cpassword=cpassword)
    
    return render(request,'register.html')