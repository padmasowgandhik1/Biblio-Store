from django.forms import *
from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=75,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter username'})
    )

    password = forms.CharField(
        max_length=75,
        required=True,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'enter password'})
    )

class SignupForm(forms.Form):
    first_name = forms.CharField(
        max_length=75,
        required=True,
        widget=forms.TextInput(attrs = {'class':'form-control','placeholder':'enter first name'})
    )

    last_name = forms.CharField(
        max_length=75,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter last name'})
    )

    username = forms.CharField(
        max_length=75,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter username'})
    )

    password = forms.CharField(
        max_length=75,
        required=True,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'enter password'})
    )
