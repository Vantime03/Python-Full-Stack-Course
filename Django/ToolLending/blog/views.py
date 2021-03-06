from django.shortcuts import render
from .models import Post

# Create your views here.

posts = [
    {
        'author': 'System Administrator',
        'title': 'System Test: First Post Test',
        'content': 'This is first post test uploaded by system administrator.',
        'date_posted': 'December 1, 2019',
    },
    {
        'author': 'Vantime',
        'title': 'Django Learning Update: video 3',
        'content': 'I\'ve been learning django tutorial video from Corey Schafer. I\'m on tutorial video #3 which can be found here https://www.youtube.com/watch?v=qDwdMDQ8oX4',
        'date_posted': 'December 1, 2019',
    }
]

def home(request):
    return render(request, 'blog/home.html', {'title': 'Home'})

def blog(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/blog.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About Us'})
