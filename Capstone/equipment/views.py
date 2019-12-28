from django.shortcuts import render
from .models import Equipment

def home(request): 

    context = {
        'equipments': Equipment.objects.filter(available=True)
    }

    return render(request, 'landing_page/home.html', context)

def about(request): 
    return render(request, 'landing_page/about.html', {'title': 'About'})

# def home(request):
#     return render(request, 'landing_page/home.html', {'title': 'home page'})