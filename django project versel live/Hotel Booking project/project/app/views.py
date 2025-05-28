from django.shortcuts import render,redirect
from .models import Client,Query
from django.urls import reverse


def home(request):
    return render(request,'home.html')
def about(request):
    return render(request,'about.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        msg = "Message Send Successfully"
        return render(request, 'contact.html', {'msg': msg, 'msg_type': 'success'})

    return render(request, 'contact.html')


def gallery(request):
    return render(request,'gallery.html')
def services(request):
    return render(request,'services.html')
def book_event(request):
    return render(request,'book_event.html')
def book_room(request):
    return render(request,'book_room.html')

def register(request):
    if request.method=='POST':

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
                Client.objects.create(clt_username=username,clt_email=email,clt_phone=phone,clt_dob=dob,clt_gender=gender,clt_image=image,clt_detail=detail,clt_password=password,clt_cpassword=cpassword)
                msg = "Registered Successfully!"
                return render(request, 'login.html', {'msg': msg, 'msg_type': 'success'})
            else:
                msg="Password and Confirm password not match"
                userdata={'username':username,'email':email,'phone':phone,'detail':detail}
                return render(request,'register.html',{'msg':msg,'msg_type': 'password_mismatch','data':userdata})
            
    else:
        return render(request,'register.html')

def login(request):
    # Admin login code Start here
    adminemail='admin325@gmail.com'
    adminpass='ajay123'
    if request.method=='POST':
        em=request.POST.get('email')
        ps=request.POST.get('password')
        if em==adminemail and ps==adminpass:
            return redirect('admindash')
        # Admin login code End here

        # User login code start here 
        eml=request.POST.get('email')
        psw=request.POST.get('password')
        user=Client.objects.filter(clt_email=eml)

        if user:
            userdata=Client.objects.get(clt_email=eml)
            psw1=userdata.clt_password
            if psw==psw1:
                msg="Login Successfully"
                return render(request,'dashboard.html',{'userdata':userdata,'msg':msg,'msg_type': 'success','dashboard': True})
            
            else:
                msg="Passwords don’t match"
                return render(request,'login.html',{'email':eml,'msg':msg,'msg_type': 'password_mismatch'})

        else:
            msg="Email address not found."
            return render(request,'register.html',{'msg':msg,'msg_type': 'email_error'})
        
        # User login code Ende here 

        # Admin login code start here
    elif request.method=='POST':
        
        
        if em==adminemail and ps==adminpass:
            return redirect('admindash')

    else:
        return render(request,'login.html')
    
    
def home1(request,pk):
    userdata=Client.objects.get(id=pk)
    return render(request,'home.html',{'userdata':userdata})

def about1(request,pk):
    userdata=Client.objects.get(id=pk)
    return render(request,'about.html',{'userdata':userdata})

def gallery1(request,pk):
    userdata=Client.objects.get(id=pk)
    return render(request,'gallery.html',{'userdata':userdata})

def services1(request,pk):
    userdata=Client.objects.get(id=pk)
    return render(request,'services.html',{'userdata':userdata})

def contact1(request,pk):
    userdata=Client.objects.get(id=pk)
    return render(request,'contact.html',{'userdata':userdata})

def book_event1(request,pk):
    userdata=Client.objects.get(id=pk)
    return render(request,'book_event.html',{'userdata':userdata})

def book_room1(request,pk):
    userdata=Client.objects.get(id=pk)
    return render(request,'book_room.html',{'userdata':userdata})

def dashboard(request,pk):
    userdata=Client.objects.get(id=pk)
    return render(request,'dashboard.html',{'userdata':userdata,'dashboard': True})

def admindash(request):
    return render(request,'admindash.html')


def query(request,pk):
    userdata=Client.objects.get(id=pk)

    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        query=request.POST.get('query')

        Query.objects.create(stu_name=name,stu_email=email,stu_query=query)
        msg = "Query Send Successfully"
        querydetail=Query.objects.filter(stu_email=userdata.clt_email)
        
        
        return render(request,'dashboard.html',{'userdata':userdata,'msg': msg, 'msg_type': 'success','dashboard': True})
        
    
    else:
        return render(request,'dashboard.html',{'userdata':userdata,'query':userdata})

def allquery(request,pk):
    userdata=Client.objects.get(id=pk)
    x=userdata.clt_email
    querydetail=Query.objects.filter(stu_email=x)
    return render(request,'dashboard.html',{'userdata':userdata,'querydetail':querydetail})

def edit(request,pk):
    editdata=Query.objects.get(id=pk)
    email=editdata.stu_email
    userdata=Client.objects.get(clt_email=email)
    return render(request,'dashboard.html',{'userdata':userdata,'editdata':editdata})

def queryupdate(request,pk):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        query=request.POST.get('query')
        old_query=Query.objects.get(id=pk)
        old_query.stu_name=name
        old_query.stu_email=email
        old_query.stu_query=query
        old_query.save()
        querydetail=Query.objects.filter(stu_email=email)
        userdata=Client.objects.get(clt_email=email)
        return render(request,'dashboard.html',{'userdata':userdata,'querydetail':querydetail})
    
def delete(request,pk):
    deledata=Query.objects.get(id=pk)
    email=deledata.stu_email
    deledata.delete()
    querydetail=Query.objects.filter(stu_email=email)
    userdata=Client.objects.get(clt_email=email)
    msg="Deleted Successfully"
    return render(request,'dashboard.html',{'userdata':userdata,'querydetail':querydetail,'msg': msg, 'msg_type': 'success'})

from django.db.models import Q

def search(request, pk):
    userdata = Client.objects.get(id=pk)
    searchData = request.POST.get('search')

    
    if request.POST.get('action') == "Reset All Data":
        x = userdata.clt_email
        querydetail = Query.objects.filter(stu_email=x)
        return render(request, 'dashboard.html', {
            'userdata': userdata,
            'querydetail': querydetail,
        })

    
    all_data = Query.objects.filter(
        Q(stu_name__icontains=searchData) |
        Q(stu_email__icontains=searchData) |
        Q(stu_query__icontains=searchData)
    )

    return render(request, 'dashboard.html', {
        'userdata': userdata,
        'querydetail': all_data, 
        'searchData': searchData
    })


