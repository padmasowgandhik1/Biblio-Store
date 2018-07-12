from django import forms
from booksapp.models import *

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['id','user_pf']