from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from shop.models import Product
from .cart import Cart
from .forms import AddToCartForm
# Create your views here.
@require_POST

def cart_add(request, product_id=None):
    cart = Cart(request)
    product = get_object_or_404(Product, id = product_id)
    form = AddToCartForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product = product, quantity = cd['quantity'], update_quantity = cd['update'])
    print(cart)
    return redirect('cart:cart_detail')

def cart_remove(request, product_id=None):
    cart = Cart(request)
    product = get_object_or_404(Product, id = product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')

def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = AddToCartForm(initial = {'quantity': item['quantity'], 'update': True } )
    return render(request, 'cart/cart_detail.html', {'cart':cart})

def product_detail(request, id=None):
    product = Product.objects.get(pk=id)
    cart_product_form = AddToCartForm()
    return render(request, 'shop/product_detail.html', context= {'product': product, 'cart_product_form': cart_product_form})