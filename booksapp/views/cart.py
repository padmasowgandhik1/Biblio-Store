import string
from datetime import date, datetime
from random import random

from django.contrib.messages import info
from django.core.checks import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView,CreateView,DeleteView
from booksapp.models import *

class CartListView(ListView):
    model = Order
    context_object_name = "cart"
    template_name = "booksapp/html_template/cart.html"

    def get_context_data(self, **kwargs):
        context = super(CartListView, self).get_context_data(**kwargs)

        id1 =  self.request.user.id
        order_object = Order.objects.filter(owner_id = self.request.user.id)

        cart_items =[ i.items.all() for i in order_object]
        cart_products = [j for i in cart_items for j in i]

        for j in order_object:
            total = Order.get_cart_total(j)

        context.update({
            'cart':cart_products,
            'total':total,
            'user_permissions': self.request.user.get_all_permissions
        })

        return context
    pass

def add_to_cart(request,**kwargs):
    user_profile = get_object_or_404(Profile, user_pf_id = request.user.id)
    product = Products.objects.filter(id = kwargs.get('pk',"")).first()

    order_item,status = OrderItem.objects.get_or_create(product = product)
    user_order,status = Order.objects.get_or_create(owner=user_profile)
    user_order.items.add(order_item)
    if status:
        #user_order.ref_code = generate_order_id()
        user_order.save()

    messages = info(request,"Item Added To Cart")
    return redirect(reverse("biblioapp:show_products"))

class OrderItemDeleteView(DeleteView):
    model=OrderItem
    template_name = "booksapp/cart.html"
    success_url = reverse_lazy('biblioapp:view_cart')

    def get(self,request,*args,**kwargs):
        return self.post(request,args,kwargs)

    def post(self, request, *args, **kwargs):
        self.delete(request, args, kwargs)
        return redirect('biblioapp:view_cart')



def generate_order_id():
    date_str = date.today().strftime('%Y%m%d')[2:] + str(datetime.now().second)
    rand_str = "".join([random.choice(string.digits) for count in range(3)])
    return date_str + rand_str