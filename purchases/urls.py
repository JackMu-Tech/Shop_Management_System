from django.urls import path
from .views import PurchaseListView

urlpatterns = [
    path('', PurchaseListView.as_view(), name='purchase-list'),
    # Add more paths for additional views if needed
]
