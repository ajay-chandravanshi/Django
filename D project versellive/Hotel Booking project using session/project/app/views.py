from django.shortcuts import render,redirect
from .models import Client,Query,Room
from django.urls import reverse
from urllib.parse import urlencode



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
    all_card=Room.objects.all()
    return render(request,'book_room.html',{'data':all_card})

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
    # Admin credentials
    adminemail = 'admin325@gmail.com'
    adminpass = 'ajay123'
    a_name = 'Anjali'
    a_id = 122

    if request.method == 'POST':
        em = request.POST.get('email')
        ps = request.POST.get('password')

        # Admin login check
        if em == adminemail and ps == adminpass:
            request.session['admin_id'] = a_id
            request.session['admin_name'] = a_name
            request.session['admin_email'] = adminemail
            return redirect('admindash1')

        # User login code start here 
        user = Client.objects.filter(clt_email=em)

        if user:
            userdata = Client.objects.get(clt_email=em)
            psw1 = userdata.clt_password
            if ps == psw1:
                msg = "Login Successfully"
                return render(request, 'dashboard.html', {'userdata': userdata, 'msg': msg, 'msg_type': 'success', 'dashboard': True})
            else:
                msg = "Passwords don’t match"
                return render(request, 'login.html', {'email': em, 'msg': msg, 'msg_type': 'password_mismatch'})
        else:
            msg = "Email address not found."
            return render(request, 'register.html', {'msg': msg, 'msg_type': 'email_error'})
        # User login code End here 

    return render(request, 'login.html')

# userdata code start here
    
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
    all_card=Room.objects.all()
    return render(request,'book_room.html',{'userdata':userdata,'data':all_card})

def dashboard(request,pk):
    userdata=Client.objects.get(id=pk)
    return render(request,'dashboard.html',{'userdata':userdata,'dashboard': True})

def showcard(request,pk):
    userdata=Client.objects.get(id=pk)
    cart = request.session.get('cart',[])
    # print(cart)
    all_data1 = []
    total_amt=0
    for i in cart:
        item = Room.objects.get(id=i)
        total_amt+=(item.room_price)
        all_data1.append(item)
    return render(request,'showcard.html',{'cart':all_data1,'total_amt':total_amt,'userdata':userdata})

def addcard(request,cpk,pk):
    userdata=Client.objects.get(id=pk)
    # print(pk)
    cart = request.session.get('cart',[])
    # print(cart)
    if cpk in cart:
        msg = "Already added"
        all_items = Room.objects.all()
        msg="Card Already Added"
        return render(request,'book_room.html',{'userdata':userdata,'data':all_items,'msg': msg, 'msg_type': 'email_error'})
    else:
        userdata=Client.objects.get(id=pk)
        cart.append(cpk)
        # print(cart)
        msg = 'Added Successfully...'
        request.session['cart']=cart
        all_items = Room.objects.all()
        return render(request,'book_room.html',{'data':all_items,'userdata':userdata,'msg':msg,'msg_type': 'success'})

def delete(request,cpk,pk):
    userdata=Client.objects.get(id=pk)
    cart = request.session['cart']
    print(cart)
    if cpk in cart:
        cart.remove(cpk)
    # print(cart)
    request.session['cart']=cart
    all_data = []
    total_amt=0
    for i in cart:
        item = Room.objects.get(id=i)
        total_amt+=(item.room_price)
        all_data.append(item)
    msg="Deleted Successfully"
    return render(request,'showcard.html',{'cart':all_data,'total_amt':total_amt,'userdata':userdata,'msg':msg,'msg_type': 'success'})

# user query code start here 
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
# user query code End here 
# userdata  Code End Here 

# admindata code Start Here

def admin_home(request):
    admindata = {
        'id': request.session.get('admin_id'),
        'name': request.session.get('admin_name'),
        'email': request.session.get('admin_email')
    }
    return render(request, 'home.html', {'admindata': admindata})

def admin_about(request):
    admindata = {
        'id': request.session.get('admin_id'),
        'name': request.session.get('admin_name'),
        'email': request.session.get('admin_email')
    }
    return render(request, 'about.html',{'admindata': admindata})

def admin_gallery(request):
    admindata = {
        'id': request.session.get('admin_id'),
        'name': request.session.get('admin_name'),
        'email': request.session.get('admin_email')
    }
    return render(request, 'gallery.html', {'admindata': admindata})

def admin_services(request):
    admindata = {
        'id': request.session.get('admin_id'),
        'name': request.session.get('admin_name'),
        'email': request.session.get('admin_email')
    }
    return render(request, 'services.html', {'admindata': admindata})

def admin_contact(request):
    admindata = {
        'id': request.session.get('admin_id'),
        'name': request.session.get('admin_name'),
        'email': request.session.get('admin_email')
    }
    return render(request, 'contact.html', {'admindata': admindata})

def admin_book_event(request):
    admindata = {
        'id': request.session.get('admin_id'),
        'name': request.session.get('admin_name'),
        'email': request.session.get('admin_email')
    }
    return render(request, 'book_event.html', {'admindata': admindata})

def admin_book_room(request):
    admin_id = request.session.get('admin_id')
    admindata = {
        'id': request.session.get('admin_id'),
        'name': request.session.get('admin_name'),
        'email': request.session.get('admin_email')
    }
    all_card=Room.objects.all()
    return render(request, 'book_room.html', {'admindata': admindata,'data':all_card})

def admindash1(request):
    if request.method == "GET":
        
        if 'admin_id' in request.session:
            admin_id = request.session['admin_id']
            admin_name = request.session['admin_name']
            admin_email = request.session['admin_email']
        
            admindata = {
                'id': admin_id,
                'name': admin_name,
                'email': admin_email
            }
            return render(request, 'admindash.html', {'admindata': admindata})
        else:
            return redirect('login')
    
    elif request.method == "POST":
        # room add form se aaya h
        rimage = request.FILES.get('room-image')
        rname = request.POST.get('room_name')
        rprice = request.POST.get('room_price')
        rinfo = request.POST.get('room_info')
        print(rimage, rname, rprice, rinfo)
        Room.objects.create(room_image=rimage, room_name=rname, room_price=rprice, room_info=rinfo)
        return redirect('book_room')

    else:
        return render(request, 'login.html')


def admin_card_delete(request,pk):
    admindata = {
        'id': request.session.get('admin_id'),
        'name': request.session.get('admin_name'),
        'email': request.session.get('admin_email')
    }
    all_card=Room.objects.all()
    deledata=Room.objects.get(id=pk)
    deledata.delete()
    msg="Card Deleted Successfully"
    return render(request, 'book_room.html',{'msg':msg,'admindata': admindata,'data':all_card})


def admin_card_edit(request,pk):
    admindata = {
        'id': request.session.get('admin_id'),
        'name': request.session.get('admin_name'),
        'email': request.session.get('admin_email')
    }
    
    editdata=Room.objects.get(id=pk)
    rname=editdata.room_name
    # carddata=Room.objects.get(room_name=rname)
    return render(request, 'admindash.html',{'admindata': admindata,'editdata':editdata,'carddata':rname})

def edit(request,pk):
    editdata=Query.objects.get(id=pk)
    email=editdata.stu_email
    userdata=Client.objects.get(clt_email=email)
    return render(request,'dashboard.html',{'userdata':userdata,'editdata':editdata})

def admin_card_update(request,pk):
    admindata = {
        'id': request.session.get('admin_id'),
        'name': request.session.get('admin_name'),
        'email': request.session.get('admin_email')
    }

    if request.method=='POST':
        rimage = request.FILES.get('room-image')
        rname = request.POST.get('room_name')
        rprice = request.POST.get('room_price')
        rinfo = request.POST.get('room_info')

        old_data=Room.objects.get(id=pk)

        if rimage:
            old_data.room_image = rimage

        old_data.room_name=rname
        old_data.room_price=rprice
        old_data.room_info=rinfo
        old_data.save()
        all_card=Room.objects.all()
        carddetail=Room.objects.filter(room_name=rname)
        carddata = Room.objects.get(id=pk)

        return render(request, 'book_room.html',{'carddetail':carddetail,'carddata':carddata,'admindata':admindata,'data':all_card}) 


# def queryupdate(request,pk):
#     if request.method=='POST':
#         name=request.POST.get('name')
#         email=request.POST.get('email')
#         query=request.POST.get('query')
#         old_query=Query.objects.get(id=pk)
#         old_query.stu_name=name
#         old_query.stu_email=email
#         old_query.stu_query=query
#         old_query.save()
#         querydetail=Query.objects.filter(stu_email=email)
#         userdata=Client.objects.get(clt_email=email)
#         return render(request,'dashboard.html',{'userdata':userdata,'querydetail':querydetail})    