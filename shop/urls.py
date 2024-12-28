from django.urls import path
from .views import *



urlpatterns = [
    path('', catalog),
    path('product_detail/<int:product_id>/', product_detail, name ="product"),
    path('create_orders/<int:product_id>/', create_orders, name ="create_orders"),
    path('orders/', orders, name ="orders"),
]