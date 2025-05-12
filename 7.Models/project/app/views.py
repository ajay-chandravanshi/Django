from django.shortcuts import render
from .models import student
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
        
        if user:
            userdata=student.objects.get(stu_email=e)
            print(userdata.stu_name)
            print(userdata.stu_email)
            print(userdata.stu_password)
            p1=userdata.stu_password
            
            if p==p1:
                return render(request,'dashboard.html',{'userdata':userdata})

            else:
                pmsg="password not match"
                return render(request,'login.html',{'email':e,'pmsg':pmsg})
        else:
            msg="email not Exist",
            return render(request,'register.html',{'msg':msg})
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
    image = request.FILES.get('profile-pic')
    document = request.FILES.get('resume')
    password=request.POST.get('password')
    cpassword=request.POST.get('cpassword')
   
    print(username,email,detail,phone,dob,subscribe,gender,password,cpassword)

    user=student.objects.filter(stu_email=email)
    if user:
        msg="user already exist"
        return render(request,'register.html',{'msg':msg})
    else:
        if password==cpassword:
            student.objects.create(stu_name=username,stu_email=email,stu_dis=detail, stu_contact=phone,stu_dob=dob,stu_quali=subscribe,stu_gender=gender, stu_image=image,stu_document=document,stu_password=password)

            msg="Registration successfully"
            return render(request,'login.html',{'msg':msg})
        else:
            msg="Password and CPassword is not matched"
            userdata={'username':username,'email':email,'detail':detail,'phone':phone,'dob':dob,'subscribe':subscribe,'gender':gender,'image':image,'document':document}
            return render(request,'register.html',{'msg':msg,'data':userdata})
