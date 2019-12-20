from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('list/', views.list, name='list'),
    path('list/<int:id>', views.detail, name='detail'),
    path('create/', views.create, name='create'),
]


