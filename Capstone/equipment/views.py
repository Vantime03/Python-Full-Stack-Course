from django.shortcuts import render
from django.http import HttpResponse

def home(request): 

    context = {
        'posts': posts
    }

    return render(request, 'landing_page/home.html', context)

def about(request): 
    return render(request, 'landing_page/about.html', {'title': 'About'})

# def home(request):
#     return render(request, 'landing_page/home.html', {'title': 'home page'})