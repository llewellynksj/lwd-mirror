from django.urls import path
from . import views

urlpatterns = [
    path(
        '',
        views.DisplayHomepage,
        name='index'),
    path(
        'products/',
        views.ProductList.as_view(),
        name='products'),
    path(
        'category/<str:selected_cat>/',
        views.CategoryProducts,
        name='category'),
    path(
        'product/<int:pk>',
        views.ProductDetails.as_view(),
        name='product_details'),
    path(
        'like/<int:pk>',
        views.CustomerFavourites,
        name='customer_fav'),
]
