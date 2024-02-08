from django.urls import path
from .views import SupplierListView

urlpatterns = [
    path('', SupplierListView.as_view(), name='supplier-list'),
    # Add more paths for additional views if needed
]
