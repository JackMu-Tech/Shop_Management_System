from django.db import models
from customers.models import Customer
from inventory.models import Product

class Sale(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    total_amount = models.DecimalField(max_digits=10,decimal_places=2)
    sales_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.customer} - {self.product} - {self.quantity} units"
