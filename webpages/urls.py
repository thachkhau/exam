from django.contrib import admin
from django.urls import path
from webpages import views
from django.conf.urls import url
app_name = 'webpage'

urlpatterns = [
    url(r'^gioithieu/$', views.blog_detail, name='gioithieu'),
    url(r'^giaohang/$', views.blog, name='giaohang'),
    url(r'^contact/$', views.contact, name='contact'),
]
