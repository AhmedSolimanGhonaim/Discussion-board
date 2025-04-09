from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Profile

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

class ProfileUpdateForm(forms.ModelForm):
    bio = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control bg-light border-0',
            'rows': 4,
            'placeholder': 'Tell us about yourself...'
        }),
        required=False
    )
    
    avatar = forms.ImageField(
        widget=forms.FileInput(attrs={
            'class': 'form-control bg-light border-0',
            'accept': 'image/*'
        }),
        required=False
    )

    class Meta:
        model = Profile
        fields = ['avatar', 'bio']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['avatar'].help_text = 'Upload a square image for best results'
        self.fields['bio'].help_text = 'Maximum 500 characters'