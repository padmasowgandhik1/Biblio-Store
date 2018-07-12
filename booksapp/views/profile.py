from django.shortcuts import render, redirect
from django.views.generic import View, UpdateView, ListView, CreateView
from requests import request

from booksapp.models import Profile
from booksapp.views import *

class ProfileView(View):
    def get(self,*args,**kwargs):
        prof_info = Profile.objects.all()

        return render( request,
           template_name= 'booksapp/profile.html',
           context = {
               'prof': prof_info
           })
    pass

class ProfileListView(ListView):
    model = Profile
    context_object_name = "prof"
    template_name = 'booksapp/profile.html'

    def get_context_data(self, **kwargs):
        context = super(ProfileListView, self).get_context_data(**kwargs)
        prof = Profile.objects.filter(user_pf_id = self.request.user.id)
        context.update({
            'prof': prof,
            'user_permissions': self.request.user.get_all_permissions
        })
        return context

class CreateProfileView(CreateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'booksapp/profile_form.html'

    def get_context_data(self, **kwargs):
        context = super(CreateProfileView, self).get_context_data(**kwargs)
        context.update({
            'prof': context.get('form'),
        })
        return  context

    def post(self, request, *args, **kwargs):
        user_pf = get_object_or_404(User, id=self.request.user.id)
        prof_form = ProfileForm(request.POST)

        if prof_form.is_valid():
            profile = prof_form.save(commit=False)
            profile.user_pf = user_pf
            profile.save()

        return redirect('biblioapp:show_products')





class UpdateProfileView(UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'booksapp/profile_form.html'
    success_url = reverse_lazy('biblioapp:show_products')

    def get_object(self, queryset=None):
        #return update_or_create(Profile, **self.kwargs)
        return get_object_or_404(Profile, **self.kwargs)

    def get_context_data(self, **kwargs):
        context = super(UpdateProfileView, self).get_context_data(**kwargs)

        context.update({
            'user_permissions': self.request.user.get_all_permissions()
        })
        return context

        pass
# class UpdateProfileView(UpdateView):
#     model = Profile
#     form_class = ProfileForm
#     template_name = 'booksapp/profile_form.html'
#     success_url = reverse_lazy('biblioapp:show_products')
#
#     def get_object(self, queryset=None):
#         return get_object_or_404(Profile,**self.kwargs)
#
#     def get_context_data(self, **kwargs):
#         context = super(UpdateProfileView, self).get_context_data(**kwargs)
#         #prof = Profile.objects.filter(user_pf_id=self.request.user.id)
#         #pf_form = context.get('profile')
#
#         context.update({
#             #'pf_form':context.get('form'),
#             'user_permissions': self.request.user.get_all_permissions()
#         })
#         return context
#
# #     def get_context_data(self, **kwargs):
# #         context = super( UpdateProfileView, self).get_context_data(**kwargs)
# #
# #         import ipdb
# #         ipdb.set_trace()
# #
# #         context.update({
# #             'prof': context.get('form'),
# #         })
# #         return context
# #
#     def post(self, request, *args, **kwargs):
#         user_pf = get_object_or_404(User, id=self.request.user.id)
#         prof_form = ProfileForm(request.POST)
#
#         if prof_form.is_valid():
#             profile = prof_form.save(commit=False)
#             profile.user_pf = user_pf
#             profile.save()
#
#         return redirect('biblioapp:show_products')
#

# class UpdateProfileView(UpdateView):
#     template_name = 'booksapp/profile_update.html'
#     success_url = reverse_lazy('biblioapp:show_products')
#
#     def get_object(self):
#         return self.request.user.profile

