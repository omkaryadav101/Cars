from django.shortcuts import render, get_object_or_404
from .models import Kar


def home(request):
    kars= Kar.objects.all()
    return render(request, 'home.html', {'kars': kars})

def car_detail(request, car_id):
    car = get_object_or_404(Kar, pk=car_id)
    return render(request, 'car_detail.html', {'car': car})

# Create your views here.
