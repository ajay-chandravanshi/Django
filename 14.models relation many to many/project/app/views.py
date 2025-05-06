from django.shortcuts import render
from .models import Vehicles
# Create your views here.

def vehical(request):
    data = Vehicles.objects.all()
    print(data)
    print(data.values())
    print(data.values_list())

    details = Vehicles.objects.get(id=1)
    print(details.Vehicle_name)
    x = details.Fuel_name.all()

