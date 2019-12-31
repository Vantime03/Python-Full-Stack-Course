from django.shortcuts import render, redirect
from .models import short_URL
from .forms import UrlForm
from .shortener import Shortener


def Home(request, token):
     long_url = short_URL.objects.filter(short_url=token)[0]
     return redirect(long_url)

def Make(request):
     form = UrlForm(request.POST)
     a = ''

     if request.method == 'POST':
          if form.is_valid():
               NewURL = form.save(commit=False)
               a = Shortener().issue_token()
               NewURL.short_URL = a
               NewURL.save()
          else:
               form = UrlForm()
               a = 'Invalid URL'
     return render(request, 'home.html', {'form': form, 'a': a})
