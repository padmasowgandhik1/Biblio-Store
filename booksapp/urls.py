from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path
from booksapp import views
from booksapp.views import *
from hackthon_day import settings

app_name = 'biblioapp'

urlpatterns = [
    path('signup/', SignupControler.as_view(), name="sign_up"),
    path('login/', LoginController.as_view(), name="log_in"),
    path('logout/', logout_user, name="log_out"),

    path('profile/', ProfileListView.as_view(), name="view_profile"),
    path('profile/add', CreateProfileView.as_view(), name="add_profile"),
    path('profile/<int:pk>/update', UpdateProfileView.as_view(), name='update_profile'),
    #path('profile/update', UpdateProfileView.as_view(), name='update_profile'),

    path('cart/',CartListView.as_view(),name='view_cart'),
    path('cart/<int:pk>/add',add_to_cart,name='add_to_cart'),
    path('prod_del/<int:pk>', OrderItemDeleteView.as_view(), name='cart_product_delete'),

    path('ratings/<int:pk>', CreateReviewsView.as_view(),name='ratings'),

    path('product/<int:pk>/', ProductView.as_view(), name="view_product"),
    path('product/<int:pk>', ProductViewAndSimilar.as_view(), name="view_product_and_similar_prods"),
    path('product/', SearchProductView.as_view(), name="searched_product"),
    path('product/<str:category>', search_by_category_view.as_view(), name="category_searched_product"),
    path('product/subcategory/<str:subcategory>',search_by_subcategory_view.as_view(), name="subcategory_searched_product"),
    path('products/', ProductListView.as_view(), name="show_products"),
    path('home/products/', ProductListViewAfterLogin.as_view(), name="show_products_after_login"),
    path('products/add', CreateProductView.as_view(), name="add_product"),
    path('products/<int:pk>/delete', DeleteProductView.as_view(), name='delete_product'),
    path('products/<int:pk>/update', UpdateProductView.as_view(), name='update_product'),
    ]