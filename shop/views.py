from django.shortcuts import render
from django.core.paginator import Paginator
from shop.models import Product
from cart import forms

# Create your views here.
def index(request):
    pro_list = Product.objects.order_by('ten_sp')
    paginator = Paginator(pro_list, 8)
    page = request.GET.get('page')
    pro_dict = paginator.get_page(page)
    for i in paginator.page_range:
        print(i)
    return render(request, 'shop/index.html', {'products': pro_dict})

def product_detail(request, id=None):
    product = Product.objects.get(pk=id)
    cart_product_form = forms.AddToCartForm()
    return render(request, 'shop/product_detail.html', context= {'product': product, 'cart_product_form': cart_product_form, 'title': "Chi Tiết Sản Phẩm"})

def product(request):
    pro_list = Product.objects.order_by('ten_sp')
    paginator = Paginator(pro_list, 8)
    page = request.GET.get('page')
    pro_dict = paginator.get_page(page)
    return render(request, 'shop/product.html', {'products': pro_dict, 'title': "Sản Phẩm"})
