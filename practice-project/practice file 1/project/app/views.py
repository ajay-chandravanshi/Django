from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    x="<h1>hello sir....<h1/>"
    return HttpResponse(x)

def index(request):
    return render(request,'index.html')
