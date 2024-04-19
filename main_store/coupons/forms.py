from django import forms


class CouponApplyForm(forms.Form):
    code = forms.CharField(max_length=100 , widget=forms.TextInput(attrs={
    'placeholder':"Coupon Code",
     'class':"form-control border-0 p-4",

    }))