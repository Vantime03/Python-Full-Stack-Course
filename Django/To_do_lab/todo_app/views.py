from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Todo
from django.http import Http404

def home(request):
    return HttpResponse("This is Home Page")

def list(request):
    context = {
        'Tasks': Todo.objects.all()
    }
    return render(request, 'todos/list.html', context)

def detail(request, id):
    try:
        task = Todo.objects.get(pk=id)
    except Todo.DoesNotExist:
        raise Http404("Task does not exist")
    return render(request, 'todos/detail.html', {'task': task})

def create(request):
    if request.method == 'GET':
        return render(request, 'todos/create.html')
    elif request.method == 'POST':
        title_field = request.POST['title']
        text_field = request.POST['text']
        if request.POST['status'] == 'False':
            status_field = False
        else:
            status_field = True
        todo = Todo.objects.create(title = title_field, text = text_field, status = status_field)
        return redirect('list')

