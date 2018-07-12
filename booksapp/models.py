from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    name = models.CharField(max_length=50)
    profilepassword = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=10)

    user_pf = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Products(models.Model):
    name = models.CharField(max_length=255)
    pic = models.ImageField(upload_to='product_pic',blank=True)
    cost = models.IntegerField()
    status = models.BooleanField(default=False)
    category = models.CharField(max_length=255,default = 'books')
    subcategory = models.CharField(max_length=255,default = 'books')

    def __str__(self):
        return self.name

class Cart(models.Model):
    name = models.CharField(max_length=255)
    pic = models.CharField(max_length=255)
    cost = models.IntegerField()
    status = models.BooleanField(default=False)

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class OrderItem(models.Model):
     product = models.OneToOneField(Products,on_delete=models.SET_NULL,null=True)
     is_orderd = models.BooleanField(default=False)
     date_added = models.DateTimeField(auto_now=True)
     date_ordered = models.DateTimeField(null=True)

     def __str__(self):
         return self.product.name


class Order(models.Model):
    ref_code = models.CharField(max_length=15)
    owner = models.ForeignKey(Profile,on_delete=models.SET_NULL,null=True)
    is_ordered = models.BooleanField(default=False)
    items = models.ManyToManyField(OrderItem)
    date_ordered = models.DateTimeField(auto_now=True)

    def get_cart_items(self):
        return self.items.all()

    def get_cart_total(self):
        return sum([item.product.cost for item in self.items.all() if(item.product)])

    def __str__(self):
        return '{0}-{1}'.format(self.owner,self.ref_code)

class Ratings_Reviews(models.Model):
    #product = models.ForeignKey(Products,on_delete=models.SET_NULL,null=True)
    p_id = models.IntegerField()
    u_id = models.IntegerField()
    rr_uname = models.CharField(max_length=255)
    ratings = models.IntegerField()
    review = models.CharField(max_length=255)

    def __str__(self):
        return self.rr_uname


