from django.contrib import admin
from webpages.models import Contact, Blog, Blogtype
# Register your models here.
admin.site.register(Contact)
admin.site.register(Blog)
admin.site.register(Blogtype)