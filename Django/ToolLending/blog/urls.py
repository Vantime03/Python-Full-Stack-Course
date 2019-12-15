from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='toolLending-home'),
    path('blog/', views.blog, name = 'toolLending-blog'),
    path('about/', views.about, name='toolLending-about'),
]