from django import forms
from booksapp.models import *

class RatingsReviewsForm(forms.ModelForm):
    class Meta:
        model = Ratings_Reviews
        exclude = ['id','u_id','p_id','rr_uname']