from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    x="<h1 style='color:red'>Hello...</h1>"
    y="<div style='border:2px'>Hello sir..</div>"
    return HttpResponse(y)