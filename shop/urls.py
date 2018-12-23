from django.contrib import admin
from django.urls import path
from shop import views
from django.conf.urls import url
app_name = 'shop'

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^product_detail/(\d+)/$', views.product_detail, name='product_detail'),
    url(r'^product/$', views.product, name='product'),
]
