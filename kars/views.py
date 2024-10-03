from django.shortcuts import render, get_object_or_404
from .models import Kar

# Home view to display the list of cars
def home(request):
    cars = Kar.objects.all()
    return render(request, 'home.html', {'cars': cars})

# Detail view to display a specific car's details
def car_detail(request, car_id):
    car = get_object_or_404(Kar, pk=car_id)
    return render(request, 'car_detail.html', {'car': car})
