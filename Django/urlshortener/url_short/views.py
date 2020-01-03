from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from .models import Todo
import random
import string

###This section will create a random generate URL
def generate_short_url():
    charlist = string.ascii_letters + string.digits
    short_url = ''
    for i in range (6):
        char = random.choice(charlist)
        short_url += char
    return short_url

def home(request):
    context = {
        'short_url': Todo.objects.all()
    }
    return render(request, 'main.html', context)

def create(request):
    if request.method == 'GET':
        return render(request, 'create.html')
    elif request.method == 'POST':
        url = request.POST['url']
        code = generate_short_url()
        new_url = Todo.objects.create(code = code, url = url)
        new_url.save()
        return redirect('home')   

def direct(request, code):
    print(code)
    try:
        get_url = Todo.objects.get(code=code)
    except Todo.DoesNotExist:
        raise Http404("short url does not exist")
    return redirect(get_url.url)

