from django import forms
from store.models import Product
from orders.models import Order 

from django.utils.text import slugify

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'seller' ,'category','status', 'image', 'description', 'price', 'old_price', 'stock', 'available' ]
        widgets = {
            "name": forms.TextInput(attrs={'class': 'form-control'}),
            "seller": forms.Select(attrs={'class': 'form-control'}),
            "category": forms.Select(attrs={'class': 'form-control'}),
            "status": forms.Select(attrs={'class': 'form-control'}),\
            "image": forms.FileInput(attrs={'class': 'form-control'}),
            "description": forms.TextInput(attrs={'class': 'form-control'}),
            "price": forms.NumberInput(attrs={'class': 'form-control'}),
            "old_price": forms.NumberInput(attrs={'class': 'form-control'}),
            "stock": forms.NumberInput(attrs={'class': 'form-control'}),
            "available": forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

    def save(self, commit=True):
        instance = super(ProductForm, self).save(commit=False)
        instance.slug = slugify(instance.name)  # Generate slug from the name field
        if commit:
            instance.save()
        return instance
    

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name' , 'last_name' , 'email' , 'address' , 'phone' , 'postal_code' , 'notes', 'city' , 'paid']

        widgets = {
            "first_name": forms.TextInput(attrs={'class': 'form-control'}),
            "last_name": forms.TextInput(attrs={'class': 'form-control'}),
            "email": forms.EmailInput(attrs={'class': 'form-control'}),
            "address": forms.TextInput(attrs={'class': 'form-control'}),
            "phone": forms.NumberInput(attrs={'class': 'form-control'}),
            "postal_code": forms.NumberInput(attrs={'class': 'form-control'}),
            "notes": forms.TextInput(attrs={'class': 'form-control'}),
            "city": forms.TextInput(attrs={'class': 'form-check-input'}),
            "paid": forms.CheckboxInput(attrs={'class': 'form-check-input'}),

        }




