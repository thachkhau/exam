from django.contrib import admin
from django.urls import path
from customers import views
from django.conf.urls import url
app_name = 'customers'

urlpatterns = [
    url(r'^dang_nhap/$', views.dang_nhap, name='dang_nhap'),
    url(r'^dang_ky/$', views.dang_ky, name='dang_ky'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'dang_xuat/$', views.dang_xuat, name = 'dang_xuat'),
]
