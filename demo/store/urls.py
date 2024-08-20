from django.urls import path
from . import views, api_views

urlpatterns = [
    # API URLs
    path('api/v1/products/', api_views.ProductList.as_view(), name='product-list'),
    path('api/v1/products/new/', api_views.ProductCreate.as_view(), name='product-create'),
    path('api/v1/products/<int:id>/destroy/', api_views.ProductDestroy.as_view(), name='product-destroy'),

    # Regular URLs
    path('products/<int:id>/', views.show, name='show-product'),
    path('cart/', views.cart, name='shopping-cart'),
    path('', views.index, name='list-products'),  # This is the root URL for the store app
]
