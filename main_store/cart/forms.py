from django import forms
from coupons.forms import CouponApplyForm

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1,51)]


class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES , coerce=int ,widget=forms.Select(attrs={'class': 'form-control' }) , label='')
    override = forms.BooleanField(required=False , initial=False , widget=forms.HiddenInput)
    
