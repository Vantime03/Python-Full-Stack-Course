from django.shortcuts import render
from django.http import HttpResponse
from .models import Todo

def home(request):
    return HttpResponse("This is Home Page")

def list(request):
    context = {
        'Tasks': Todo.objects.all()
    }
    return render(request, 'todos/list.html', context)
