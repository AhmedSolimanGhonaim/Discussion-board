from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class SignUpForm(UserCreationForm):
    
    email = forms.CharField(
        max_length=254,
        required=True,
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter email'
        })
    )
    class  Meta:
        model = User
        fields = ['username' , 'email' , 'password1' , 'password2']


        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['username'].widget.attrs.update({
                'class': 'form-control',
                'placeholder': 'Choose username'
            })
            self.fields['password1'].widget.attrs.update({
                'class': 'form-control',
                'placeholder': 'Enter password'
            })
            self.fields['password2'].widget.attrs.update({
                'class': 'form-control',
                'placeholder': 'Confirm password'
            }) 