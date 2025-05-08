from django.shortcuts import render
from .models import Vehicles,Fuel
# Create your views here.

def vehical(request):
    data = Vehicles.objects.all()
    print(data)
    print(data.values())
    print(data.values_list())
    details = Vehicles.objects.get(id=1)
    print(details.Vehicle_name)
    x = details.Fuel_name.all()
    for i in x:
        print(i.Fuel_name)
def fuel(request):
    data = Fuel.objects.all()
    print(data)
    print(data.values())
    print(data.values_list())
    fuel_data = Fuel.objects.get(id=1)
    x = fuel_data.vehical.all()
    for i in x:
        print(i)



    