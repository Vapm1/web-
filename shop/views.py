from django.shortcuts import render

from .models import *
# Create your views here.
def catalog(request):
    products = Product.objects.all()
    return render(request, 'shop/catalog.html', {'products':products})  
def product_detail(request, product_id):
    product = Product.objects.get(id=product_id)
    return render(request, 'shop/product_detail.html', {'product':product})
def create_orders(request, product_id):
    if request.method == 'POST':
        address = request.POST['address']
        card = request.POST['card']
        email = request.POST['email']
        discount = request.POST['discount']
        Order.objects.create(
            adres = address,
            email = email,
            bank_card = card,
            count = discount,
            product = Product.objects.get(id=product_id)
        )
    return render(request, 'shop/create_orders.html')
def orders(request):
     orders = Order.objects.all()
     return render(request, 'shop/orders.html', {'orders':orders})  