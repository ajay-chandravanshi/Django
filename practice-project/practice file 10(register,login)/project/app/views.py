from django.shortcuts import render
from .models import student
# Create your views here.

def home(request):
    return render(request,'home.html')
def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html')
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
    detail=request.POST.get('detail')
    phone=request.POST.get('phone')
    dob=request.POST.get('dob')
    subscribe=request.POST.getlist('subscribe')
    gender=request.POST.get('gender')
    image = request.FILES.get('profile-pic')
    document = request.FILES.get('resume')
    password=request.POST.get('password')
    cpassword=request.POST.get('cpassword')

    print(username,email,detail,phone,dob,subscribe,gender,password,image,document)
    user=student.objects.filter(stu_email=email)
    if user:
        msg="User already Registered"
        return render(request,'register.html',{'msg':msg})
    else:
        if password==cpassword:
            student.objects.create(stu_name=username,stu_email=email,stu_detail=detail,stu_phone=phone,stu_dob=dob,stu_subscribe=subscribe,stu_gender=gender,stu_image=image,stu_document=document,stu_password=password)
            msg="registration Successfully"
            return render(request,'login.html',{'msg':msg})
        else:
            pmsg="password and cpassword not match"
            userdata={'username':username,'email':email,'detail':detail,'phone':phone,'dob':dob,'subscribe':subscribe,'gender':gender,'image':image,'document':document}
            return render(request,'register.html',{'pmsg':pmsg,'data':userdata})