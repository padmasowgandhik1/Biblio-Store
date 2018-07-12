from booksapp.views import *
from booksapp.models import *
from booksapp.forms import *
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.views.generic import ListView,CreateView,UpdateView,DeleteView,View
from django.shortcuts import *


class search_by_category_view(ListView):
    def get(self, request, *args, **kwargs):
        prod = Products.objects.filter(**{'category': self.kwargs.get('category')})

        return render(
            request,
            template_name='booksapp/html_template/products.html',
            context={
                'prod': prod
            }
        )
    pass


class search_by_subcategory_view(ListView):
    def get(self, request, *args, **kwargs):
        prod = Products.objects.filter(**{'subcategory': self.kwargs.get('subcategory')})

        return render(
            request,
            template_name='booksapp/html_template/products.html',
            context={
                'prod': prod
            }
        )
    pass