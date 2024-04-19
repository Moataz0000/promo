from django.db import models
from store.models import Product
import datetime
from decimal import Decimal
from django.conf import settings


class Order(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    address = models.CharField(max_length=250)
    phone = models.IntegerField(default=0)
    postal_code = models.CharField(max_length=20)
    city = models.CharField(max_length=100)
    notes = models.CharField(max_length=500 , blank=True , null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    paid = models.BooleanField(default=False) # the Pay


    class Meta:
        ordering = ['-created']
        indexes = [
            models.Index(fields=['-created']),
        ]

    def __str__(self):
        return f"Order {self.id}"
    
    def get_tax(self):
        total = self.get_total_cost()
        tax_rate = Decimal(1.5)  # Assuming 1.5% tax rate, modify as needed
        tax = (tax_rate / 100) * total
        rounded_tax = round(tax, 2)

        return rounded_tax
  

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())      
    

    
    def total_after_discount_with_tax(self):
        return self.get_tax() + self.get_total_cost()
    


class OrderItem(models.Model):
    class Status(models.TextChoices):
        Rejection = 'REJECTION', 'REJECTION'
        Pending = 'PENDING', 'PENDING'
        Shipping = 'SHIPPING', 'SHIPPING'
        
    order = models.ForeignKey(Order , on_delete=models.CASCADE , related_name="items")
    product = models.ForeignKey(Product , on_delete=models.CASCADE , related_name="oreder_items")
    price = models.DecimalField(max_digits=10 , decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)
    status = models.CharField(choices=Status.choices , max_length=10, default=Status.Pending )
    created = models.DateTimeField(auto_now_add=True , null=True)
    order_date = models.DateField(auto_now=True)

    def __str__(self):
        return str(self.id)
    
    def get_cost(self):
        return self.price * self.quantity
