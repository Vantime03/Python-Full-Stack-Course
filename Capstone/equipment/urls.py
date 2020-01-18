from django.urls import path
from .views import EquipmentDetailView, EquipmentCreateView, EquipmentUpdateView, EquipmentDeleteView, EquipmentListView, UserEquipmentListView
from . import views

urlpatterns = [
    path('', EquipmentListView.as_view(), name='home'),
    path('user/<str:username>', UserEquipmentListView.as_view(), name='user-equipment'),
    path('myinventory/', views.my_inventory, name='my-inventory'),
    path('myrental/', views.my_rental, name='my-rental'),
    path('filter/', views.keyword_search, name='keyword-search'),
    path('equipment/<int:pk>/', EquipmentDetailView.as_view(), name='equipment-detail'),
    path('equipment/<int:pk>/update/', EquipmentUpdateView.as_view(), name='equipment-update'),
    path('equipment/<int:pk>/delete/', EquipmentDeleteView.as_view(), name='equipment-delete'),
    path('equipment/new/', EquipmentCreateView.as_view(), name='equipment-create'),
    path('about/', views.about, name='about'),
    path('transaction_detail/<int:id>/', views.transaction_detail, name='transaction-detail'),
    path('return_detail/<int:id>/', views.return_detail, name='return-detail'),
    path('return_confirmation/<int:id>/', views.return_confirmation, name='return-confirmation'),

    path('messages_list/', views.messages_list, name='messages-list'),
    path('message_detail/<int:id>/<str:subject>', views.message_detail, name='message-detail'),
    path('message_detail/<int:id>', views.message_detail2, name='message-detail2'),





]

