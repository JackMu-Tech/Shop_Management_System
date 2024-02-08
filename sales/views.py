from django.shortcuts import render
from django.views.generic import ListView
from .models import Sale

class SaleListView(ListView):
    model = Sale
    template_name = 'sales/sale_list.html'
    context_object_name = 'sales'

