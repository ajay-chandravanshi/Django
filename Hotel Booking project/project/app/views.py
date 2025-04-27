from django.shortcuts import render

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