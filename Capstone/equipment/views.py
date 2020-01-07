from django.shortcuts import render, get_object_or_404, HttpResponse, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Equipment, User
from transaction.models import Transaction
from django.contrib.auth.decorators import login_required    


# # list view option1
# def home(request): 
#     context = {
#         'equipments': Equipment.objects.filter(available=True),        
#     }
#     return render(request, 'landing_page/home.html', context)

#list view option2
class EquipmentListView(ListView):
    model = Equipment
    template_name = 'landing_page/home.html'
    context_object_name = 'equipments'
    queryset = Equipment.objects.filter(available=True)
    paginate_by = 5

#view a list of equipment uploaded by user
class UserEquipmentListView(ListView):
    model = Equipment
    template_name = 'landing_page/user_equipment.html'
    context_object_name = 'equipments'
    queryset = Equipment.objects.filter(available=True)
    ordering = ['-date_posted']
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Equipment.objects.filter(owner=user).order_by('-date_posted')

# allow user to view their upload inventory
def my_inventory(request): 
    user_id = request.user.id
    context = {
        'equipments': Equipment.objects.filter(owner=user_id)        
    }
    return render(request, 'landing_page/my_inventory.html', context)

def keyword_search(request):
    if request.method == 'GET':
        search_key = request.GET.get('description')
        cost = float(request.GET.get('rent_cost'))
        sort = request.GET.get('sort')
        
        if cost == 0:
            result_from_tool_name = Equipment.objects.filter(available = True, tool_name__contains = search_key, rent_cost__gte = cost)
            result_from_description = Equipment.objects.filter(available = True, description__contains = search_key, rent_cost__gte = cost)
        elif cost == 5:
            result_from_tool_name = Equipment.objects.filter(available = True, tool_name__contains = search_key, rent_cost__lte = cost)
            result_from_description = Equipment.objects.filter(available = True, description__contains = search_key, rent_cost__lt = cost)
        elif cost == 10:
            result_from_tool_name = Equipment.objects.filter(available = True, tool_name__contains = search_key, rent_cost__lte = cost, rent_cost__gte = cost - 4)
            result_from_description = Equipment.objects.filter(available = True, description__contains = search_key, rent_cost__lt = cost, rent_cost__gte = cost - 4)
        elif cost == 15:
            result_from_tool_name = Equipment.objects.filter(available = True, tool_name__contains = search_key, rent_cost__lte = cost, rent_cost__gte = cost - 4)
            result_from_description = Equipment.objects.filter(available = True, description__contains = search_key, rent_cost__lt = cost, rent_cost__gte = cost - 4)
        elif cost == 16:
            result_from_tool_name = Equipment.objects.filter(available = True, tool_name__contains = search_key, rent_cost__gt = cost)
            result_from_description = Equipment.objects.filter(available = True, description__contains = search_key, rent_cost__gt = cost)

        if sort == 'HighToLow':
            context = {
                'equipments': result_from_description.union(result_from_tool_name).order_by('-rent_cost')
            }
        else:
            context = {
                'equipments': result_from_description.union(result_from_tool_name).order_by('rent_cost')
            }

        return render(request, 'landing_page/keyword_search.html', context)
    else:
        return render(request, 'landing_page/home.html')

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
        'rent_cost', 
        'available',
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

@login_required
def transaction_detail(request, id):
    if request.method == "GET":
        context = {
            'equipment': Equipment.objects.get(pk=id)
        }
        return render(request, 'transaction/transaction_detail.html', context)
    else:
        borrower_id = User.objects.get(pk=request.user.id)
        equipment_id = Equipment.objects.get(pk=id)
        
        #make the equipment avalable to false so that it won't show on home page. 
        Equipment.objects.filter(pk=id).update(available = False)

        #create the transaction
        Transaction.objects.create(borrower_id=borrower_id, equipment_id=equipment_id)
        return redirect('home')





    