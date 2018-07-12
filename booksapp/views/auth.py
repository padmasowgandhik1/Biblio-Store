from django.shortcuts import *
from booksapp.models import *
from django import forms
from booksapp.forms.auth import *
from django.urls import *
from django.views import View
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib import messages

def logout_user(request):
    logout(request)
    return redirect('biblioapp:show_products')


class SignupControler(View):
    def get(self,request,*args,**kwargs):
        form = SignupForm()
        return render(
            request,
            template_name='booksapp/signup.html',
            context={
                'form': form,'title':'signup'
            }
        )

    def post(self, request):
        form = SignupForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(**form.cleaned_data)
            user.save()
            user = authenticate(
                request,
                username=form.cleaned_data["username"],
                password=form.cleaned_data["password"]
            )

        if user is not None:
            login(request, user)
            return redirect('biblioapp:add_profile')
        else:
            messages.error(request, "invalid Credentials")
            return redirect('biblioapp:sign_up')

    pass


class LoginController(View):
    def get(self, request, *args, **kwargs):
        form = LoginForm()
        return render(
            request,
            template_name='booksapp/login.html',
            context={
                'form': form, 'title': 'login'
            }
        )

    def post(self,request):
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                request,
                username=form.cleaned_data["username"],
                password=form.cleaned_data["password"]
            )

            if user is not None:
                login(request, user)
                return redirect('biblioapp:show_products')
            else:
                messages.error(request, "Invalid Credentials")
                return redirect('biblioapp:log_in')


