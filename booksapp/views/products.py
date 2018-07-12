from booksapp.views import *
from booksapp.models import *
from booksapp.forms import *
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.views.generic import ListView,CreateView,UpdateView,DeleteView,View
from django.shortcuts import *

class ProductView(View):
    def get(self,request,*args,**kwargs):
       prod = Products.objects.filter(**{'pk': self.kwargs.get('pk')})
       revw = Ratings_Reviews.objects.filter(p_id = kwargs.get('pk'))

       import ipdb
       ipdb.set_trace()

       return render(
           request,
           template_name= 'booksapp/html_template/product-page.html',
           context = {
               'prod':prod,
               'revw':revw,
           }
       )

class ProductViewAndSimilar(View):
    def get(self,request,*args,**kwargs):
       prod = Products.objects.filter(**{'pk': self.kwargs.get('pk')})
       for i in prod:
        similar_prod = Products.objects.filter(**{'subcategory': i.subcategory})
       revw = Ratings_Reviews.objects.filter(p_id=kwargs.get('pk'))

       return render(
           request,
           template_name= 'booksapp/html_template/product-page.html',
           context = {
               'revw': revw,
               'prod':prod,
               'similar_prod': similar_prod
           }
       )

class SearchProductView(View):
        def get(self, request, *args, **kwargs):
            return render(
                request,
                template_name='booksapp/html_template/product-page.html',
                context={
                }
            )
        def post(self, request, *args, **kwargs):
            prod = Products.objects.filter(name = request.POST.get('search'))
            if prod:
                return render(
                    request,
                    template_name='booksapp/html_template/product-page.html',
                    context={
                        'prod' :prod
                    }
                )
            else:
                return HttpResponse("Product Not Found")

# def SearchProductView(request, *args, **kwargs):
#    if request.method == "POST" :
#         print(request.POST.get('search'))
#         return render(
#             request,
#             template_name='booksapp/prod.html',
#         )

class ProductListView(ListView):
    model = Products
    context_object_name = "prod"
    #template_name = "booksapp/homepage.html"
    template_name = "booksapp/html_template/index.html"
    def get_context_data(self, **kwargs):
        context = super(ProductListView,self).get_context_data(**kwargs)
        context.update({'user_permissions': self.request.user.get_all_permissions})
        return context

class ProductListViewAfterLogin(ListView):
    model = Products
    context_object_name = "prod"
    #template_name = "booksapp/homepage.html"
    template_name = "booksapp/html_template/homepage.html"
    def get_context_data(self, **kwargs):
        context = super(ProductListView,self).get_context_data(**kwargs)
        context.update({'user_permissions': self.request.user.get_all_permissions})
        return context


class CreateProductView(CreateView):
    model = Products
    form_class = ProductForm
    success_url = reverse_lazy('biblioapp:show_products')


class UpdateProductView(UpdateView):
    model = Products
    form_class = ProductForm
    template_name = 'booksapp/products_form.html'
    success_url = reverse_lazy('biblioapp:show_products')

    def get_object(self, queryset=None):
        return get_object_or_404(Products,**self.kwargs)

    def get_context_data(self, **kwargs):
        context = super(UpdateProductView, self).get_context_data(**kwargs)
        context.update({
            'user_permissions': self.request.user.get_all_permissions()
        })
        return context



class DeleteProductView(DeleteView):
    model = Products
    template_name = 'booksapp/delete_product.html'
    success_url = reverse_lazy('biblioapp:show_products')

