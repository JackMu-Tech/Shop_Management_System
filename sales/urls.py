from django.urls import path
from .views import SaleListView

urlpatterns = [
    path('', SaleListView.as_view(), name='sale-list'),
    # Add more paths for additional views if needed
]
