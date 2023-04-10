from django.urls import path
from .views import *
from django.views.generic import TemplateView
from .import views

urlpatterns = [
    path('create_product/',ProductCreateView.as_view(),name='create_product'),
    path('update_product/<int:pk>',ProductUpdateView.as_view(),name='update_product'),
    path('delete_product/<int:pk>',ProductDeleteView.as_view(),name='delete_product'),
    path('product_list/',ProductListView.as_view(),name='product_list'),
    path('product_detail/<int:pk>',ProductDetailView.as_view(),name='product_detail'),
    #path('role/',Userlog) 
    path('register/',TemplateView.as_view(template_name='product/register.html'),name='register'),  
]
