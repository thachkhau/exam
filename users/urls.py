from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from users import views
app_name = 'user'

urlpatterns = [
    url(r'^register/$', views.register, name = 'register'),
    url(r'^logout/$',views.user_logout,name='logout'),
    url(r'^login/$',views.user_login,name='login'),
]
