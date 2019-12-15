from django.shortcuts import render

posts = [
    {
        'author': 'Vantime',
        'title': 'Blog Post 1',
        'content': 'First post check-in: tutorial video #3',
        'date_posted': 'December 14, 2019',
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post check-in: tutorial video #3 | test post ',
        'date_posted': 'December 14, 2019',
    }
]
def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About Us'})
