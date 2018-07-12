from django import forms
from booksapp.models import *

class ProductForm(forms.ModelForm):
    class Meta:
        model = Products
        exclude = ['id']