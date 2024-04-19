from django import forms
from .models import Order
class OrderCreateForm(forms.ModelForm):
    class Meta:
        notes = forms.CharField(max_length=250 , widget=forms.TextInput(attrs={
        
        'placeholder': 'Enter notes',
        'class': 'form-control',
        }))
        model = Order
        fields = ['first_name' , 'last_name' , 'phone' , 'email' , 'address' , 'postal_code' , 'city' , 'notes']
    
    def __init__(self , *args , **kwargs):
        super(OrderCreateForm , self).__init__(*args , **kwargs)
        self.fields['first_name'].widget.attrs['placeholder'] = 'Enter First Name'   
        self.fields['last_name'].widget.attrs['placeholder'] = 'Enter last Name'
        self.fields['phone'].widget.attrs['placeholder'] = 'Enter Phone Number'
        self.fields['email'].widget.attrs['placeholder'] = 'Enter email'
        self.fields['address'].widget.attrs['placeholder'] = 'Enter address'
        self.fields['postal_code'].widget.attrs['placeholder'] = 'Enter postal_code'
        self.fields['city'].widget.attrs['placeholder'] = 'Enter City'
        self.fields['notes'].widget.attrs['placeholder'] = 'Enter notes here (:'


        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'

        





