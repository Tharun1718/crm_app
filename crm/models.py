from django.db import models

# Create your models here.
class Customer(models.Model):
    customer_id = models.PositiveIntegerField()
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_no = models.CharField(max_length=10)
    address =  models.CharField(max_length=100)

    def __str__(self):
        return f'Customer: {self.first_name} {self.last_name}'