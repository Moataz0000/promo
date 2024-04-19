from django import forms 
from .models import Comments



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['name' , 'email' , 'content']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control' , 'placeholder':'Your Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder':'Your Email'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder':'Comment'}),
        }


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name in self.fields:
            self.fields[field_name].label = False

