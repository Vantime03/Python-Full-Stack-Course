from django.urls import path
from .views import EquipmentDetailView, EquipmentCreateView, EquipmentUpdateView, EquipmentDeleteView, EquipmentListView, UserEquipmentListView
from . import views

urlpatterns = [
    path('', EquipmentListView.as_view(), name='home'),
    path('user/<str:username>', UserEquipmentListView.as_view(), name='user-equipment'),
    path('myinventory/', views.my_inventory, name='my-inventory'),
    path('filter/', views.keyword_search, name='keyword-search'),
    path('equipment/<int:pk>/', EquipmentDetailView.as_view(), name='equipment-detail'),
    path('equipment/<int:pk>/update/', EquipmentUpdateView.as_view(), name='equipment-update'),
    path('equipment/<int:pk>/delete/', EquipmentDeleteView.as_view(), name='equipment-delete'),
    path('equipment/new/', EquipmentCreateView.as_view(), name='equipment-create'),
    path('about/', views.about, name='about'),
]

