from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='sales/', permanent=False), name='index'),
    path('sales/', include('sales.urls')),
    path('customers/', include('customers.urls')),
    path('inventory/', include('inventory.urls')),
    path('purchases/', include('purchases.urls')),
    path('suppliers/', include('suppliers.urls')),
]
