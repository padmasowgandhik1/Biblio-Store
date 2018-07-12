from django.shortcuts import render, redirect
from django.views.generic import View, UpdateView, ListView, CreateView
from requests import request
from booksapp.models import *
from booksapp.views import *


class CreateReviewsView(CreateView):
    model = Ratings_Reviews
    form_class = RatingsReviewsForm
    template_name = 'booksapp/ratings_reviews_form.html'

    def get_context_data(self, **kwargs):
        context = super(CreateReviewsView, self).get_context_data(**kwargs)
        context.update({
            'review': context.get('form'),
        })
        return context

    def post(self, request, *args, **kwargs):
        user_profile = get_object_or_404(Profile, user_pf_id=request.user.id)
        review_form = RatingsReviewsForm(request.POST)

        if  review_form.is_valid():
            revw =  review_form.save(commit=False)
            revw.u_id = user_profile.id
            revw.rr_uname = user_profile.name
            revw.p_id = kwargs.get('pk')
            revw.save()

        return redirect('biblioapp:show_products')

    pass
