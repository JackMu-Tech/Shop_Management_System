from django.db import models
from suppliers.models import Supplier
from inventory.models import Product

class Purchase(models.Model):
    supplier = models.ForeignKey(Supplier,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    total_amount = models.DecimalField(max_digits=10,decimal_places=2)
    purchase_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.supplier} - {self.product} - {self.quantity} units"
