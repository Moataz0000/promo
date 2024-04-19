from django import forms  
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from .models import Profile


from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    username = forms.CharField(label='', widget=forms.TextInput(attrs={'class':'form-control' , 'placeholder':'User Name'}))
    password = forms.CharField(label='', widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))

   



class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-control' , 'placeholder':'Password'}))
    password2 = forms.CharField(label='Repeat Password',widget=forms.PasswordInput(attrs={'class':'form-control' ,'placeholder':'Confirm Password'}))

    class Meta:
        User = get_user_model()
        model = User
        fields = ['username', 'first_name','last_name', 'email']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'UserName'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control','placeholder':'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control','placeholder':'Last Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control','placeholder':'Email'}),
        }

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Password Don\'t Match.')
        return cd['password2']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name in self.fields:
            self.fields[field_name].label = False







class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name','last_name', 'email']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'UserName'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control','placeholder':'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control','placeholder':'Last Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control','placeholder':'Email'}),
        }



class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['photo' , 'bio']  
        widgets = {
            'photo': forms.FileInput(attrs={'class': 'form-control', 'placeholder':'Logo'}),
            'bio': forms.Textarea(attrs={'class': 'form-control','placeholder':'Bio '}),
            
        }
