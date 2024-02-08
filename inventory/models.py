from django.db import models
from suppliers.models import Supplier

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10,decimal_places=2)
    supplier = models.ForeignKey(Supplier, on_delete = models.CASCADE)

    def __str__(self):
        return self.name


