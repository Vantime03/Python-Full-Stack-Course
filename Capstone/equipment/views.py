from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Equipment

#list view option1
def home(request): 
    context = {
        'equipments': Equipment.objects.filter(available=True)
    }
    return render(request, 'landing_page/home.html', context)

#list view option2
class EquipmentListView(ListView):
    model = Equipment
    template_name = 'landing_page/home.html'
    context_object_name = 'equipments'
    ordering = ['-date_posted']

#detail view
class EquipmentDetailView(DetailView):
    model = Equipment
    template_name = 'landing_page/equipment_detail.html'
    
#create view
class EquipmentCreateView(LoginRequiredMixin, CreateView):
    model = Equipment
    template_name = 'landing_page/equipment_form.html'
    fields = [
        'tool_name', 
        'model_number', 
        'serial_number', 
        'description', 
        'rent_cost', 
        'image1',
        'image2',
        'image3'
        ]
    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)
    


       
#update view
class EquipmentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Equipment
    template_name = 'landing_page/equipment_form.html'
    fields = [
        'tool_name', 
        'model_number', 
        'serial_number', 
        'description', 
        'rent_cost', 
        'image1',
        'image2',
        'image3'
        ]
    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)
    #this method will check if the updater is the owner. 
    def test_func(self):
        equipment = self.get_object()
        if self.request.user == equipment.owner:
            return True
        return False



#delete view
class EquipmentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Equipment
    template_name = 'landing_page/equipment_confirm_delete.html'
    success_url = '/'

    #this method will check if the updater is the owner. 
    def test_func(self):
        equipment = self.get_object()
        if self.request.user == equipment.owner:
            return True
        return False




def about(request): 
    return render(request, 'landing_page/about.html', {'title': 'About'})

# def home(request):
#     return render(request, 'landing_page/home.html', {'title': 'home page'})