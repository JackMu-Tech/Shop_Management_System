from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length = 255)
    email = models.EmailField(unique = True)
    phone_number = models.CharField(max_length = 15,blank = True, null = True)

    def __str__(self):
        return self.name
