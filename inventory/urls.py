from django.urls import path
from .views import ProductListView

urlpatterns = [
    path('', ProductListView.as_view(), name='product-list'),
    # Add more paths for additional views if needed
]
