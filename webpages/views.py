from django.shortcuts import render
from webpages.forms import CreateContact

# Create your views here.
def contact(request):
    contacted = False
    if request.method == "POST":
        form = CreateContact(data=request.POST)
        if form.is_valid():
            form = form.save()
            form.save()
            contacted = True
        else:
            form = form.CreateContact()
    return render(request, 'webpages/contact.html', {'contacted':contacted, 'title': "Contact"})

def blog(request):
    return render(request, 'webpages/giaohang.html', {'title': "Giao Hàng"})

def blog_detail(request):
    return render(request, 'webpages/gioithieu.html', {'title': "Giới Thiệu"})

