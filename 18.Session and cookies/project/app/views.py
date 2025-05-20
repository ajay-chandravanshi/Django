from django.shortcuts import render

# Create your views here.
def home(req):
    # print("Hello......")
    # print(request.COOKIES)
    # print(type(request.COOKIES))
    return render(req,'app/register.html')

def register(req):
    if req.method=='POST':
        print("Hell...........")
        uname = req.POST.get('user id')
        passw = req.POST.get('p1')
        dob = req.POST.get('Brithday')
        email = req.POST.get('email')
        phone = req.POST.get('num')
        x = render(req,'app/login.html')
        x.set_cookie("name",uname)
        x.set_cookie('passw',passw)
        x.set_cookie('dob',dob)
        return x







