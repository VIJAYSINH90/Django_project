from django.urls import path
from .views import *
from django.views.generic import TemplateView

urlpatterns = [
    path('create_product/',ProductCreateView.as_view(),name='create_product'),
    path('update_product/<int:pk>',ProductUpdateView.as_view(),name='update_product'),
    path('delete_product/<int:pk>',ProductDeleteView.as_view(),name='delete_product'),
    path('product_list/',ProductListView.as_view(),name='product_list'),
    path('product_detail/<int:pk>',ProductDetailView.as_view(),name='product_detail'),
    path('cart/Add_to_cart/<int:pk>',AddToCartView.as_view(),name='addtocart'),
    path('cart/removefromcart/<int:pk>',RemoveFromCartView.as_view(),name='cart'),
    path('cart/',CartView.as_view(),name='cart'),
    
]
