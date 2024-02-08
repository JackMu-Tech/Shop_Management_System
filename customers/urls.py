from django.urls import path
from .views import CustomerListView

urlpatterns = [
    path('', CustomerListView.as_view(), name='customer-list'),
    # Add more paths for additional views if needed
]
