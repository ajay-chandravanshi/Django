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
        if request.method=='POST':
         email=request.POST.get('email')
         password=request.POST.get('password')
         print(email,password)
        else:    
         return render(request,'login.html')

def logindata(request):
       if request.method=='POST':
            e=request.POST.get('email')
            p=request.POST.get('password')
            user=student.objects.filter(stu_email=e)
            print("////////////",user)
            if user:
                userdata=student.objects.get(stu_email=e)
                print(userdata.stu_name)
                print(userdata.stu_email)
                p1=userdata.stu_password
                if p==p1:
                     return render(request,'dashboard.html',{'userdata':userdata})
                else:
                     msg="Password not match"
                     return render(request,'login.html',{'msg':msg,'email':e})
            else:
                 pmsg="Email Not Exist"
                 return render(request,'register.html',{'pmsg':pmsg})
       else:       
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
    image=request.FILES.get('profile-pic')
    document=request.FILES.get('resume')
    password=request.POST.get('password')
    cpassword=request.POST.get('cpassword')
    
    print(username,email,detail,phone,dob,subscribe,gender,image,document,password)
    
    user=student.objects.filter(stu_email=email)
    if user:
        msg="User already exist"
        return render(request,'register.html',{'msg':msg})
    else:
        if password==cpassword:
            student.objects.create(stu_name=username,stu_email=email,stu_detail=detail,stu_phone=phone,stu_dob=dob,stu_subscribe=subscribe,stu_gender=gender,stu_image=image,stu_document=document,stu_password=password)

            msg="Registration successfully"
            return render(request,'login.html',{'msg':msg})
        else:
           msg="password and cpassword not match"
           userdata={'username':username,'email':email,'detail':detail,'phone':phone,'dob':dob,'subscribe':subscribe,'gender':gender,'image':image,'document':document}
           return render(request,'register.html',{'msg':msg,'data':userdata})