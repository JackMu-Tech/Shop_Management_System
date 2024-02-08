from django.shortcuts import render
from django.views.generic import ListView
from .models import Supplier

class SupplierListView(ListView):
    model = Supplier
    template_name = 'suppliers/supplier_list.html'
    context_object_name = 'suppliers'

