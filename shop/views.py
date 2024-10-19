from django.shortcuts import render

from .models import Product
# Create your views here.
def catalog(request):
    products = Product.objects.all()
    return render(request, 'shop/catalog.html', {'products':products})  