from django.shortcuts import render
from django.views.generic import ListView
from .models import Purchase

class PurchaseListView(ListView):
    model = Purchase
    template_name = 'purchases/purchase_list.html'
    context_object_name = 'purchases'

