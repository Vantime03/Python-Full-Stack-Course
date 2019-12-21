from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Todo
from django.http import Http404
# from django.utils.datastructures import MultiValueDictKeyError

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

def update(request, id):

    if request.method == 'GET':
        task = Todo.objects.get(pk=id)
        return render(request, 'todos/update.html', {'task': task})
        
    elif request.method == 'POST':
        title_field = request.POST['title']
        text_field = request.POST['text']
        
        if request.POST['status'] == "False":
            status_field = False
        else:
            status_field = True
        
        created_date_field = request.POST['created_at']

        completed_date_field = request.POST['completed_at']
        if completed_date_field == "":
            completed_date_field = None

        Todo.objects.filter(pk=id).update(title=title_field, text=text_field, status=status_field, created_at=created_date_field, completed_at=completed_date_field)
        
        return redirect('list')

def delete(request, id):
    task = Todo.objects.get(pk=id)
    task_name = task.title
    task.delete()
    return render(request, 'todos/delete.html')


