from django.urls import path
from . import views

urlpatterns = [
    path('cart/', views.show_cart, name='cart'),
    path('add_to_cart/', views.add_to_cart, name='add_to_cart'),
    path('remove_from_cart/<id>', views.remove_from_cart, name='remove_from_cart'),
    path('update_quantity_of_cart_item/', views.update_quantity_of_cart_item, name='update_quantity'),
    path('checkout/', views.checkout, name='checkout'),
]