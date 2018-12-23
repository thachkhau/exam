from django.shortcuts import render
from customers.forms import CustomerCreate
from django.shortcuts import redirect
from customers.models import Customer
from django.contrib.auth.hashers import Argon2PasswordHasher

# Create your views here.
def dang_ky(request):
    form = CustomerCreate()
    registered = False
    if request.method == "POST":
        form = CustomerCreate(data=request.POST)
        hasher = Argon2PasswordHasher()
        if form.is_valid() and form.cleaned_data['mat_khau'] == form.cleaned_data['confirm']:
            request.POST._mutable = True
            register = form.save(commit=False)
            register.ho_ten = form.cleaned_data['ho_ten']
            register.user_name = form.cleaned_data['user_name']
            register.mat_khau = hasher.encode(form.cleaned_data['mat_khau'],'somewhere')
            register.email = form.cleaned_data['email']
            register.phone = form.cleaned_data['phone']
            register.dia_chi = form.cleaned_data['dia_chi']
            register.save()
            registered = True
            return render(request, 'customers/profile.html', {'username':register.user_name})
        elif form.cleaned_data['mat_khau'] != form.cleaned_data['confirm']:
            form.add_error('confirm', 'Mật khẩu không khớp')
        else:
           form = CustomerCreate()      
    return render(request, 'customers/dang_ky.html', {'form': form, 'registered': registered})

def dang_nhap(request):
    err = ''
    if request.session.has_key('username'):
        return redirect('customers:profile')
    elif request.method == "POST":
        hashers = Argon2PasswordHasher()
        _ten = request.POST.get('user_name')
        _mat_khau = hashers.encode(request.POST.get('mat_khau'),'somewhere')
        kh = Customer.objects.filter(user_name = _ten, mat_khau = _mat_khau)
        if kh.count() > 0:
            request.session['username'] = kh[0].ho_ten
            return redirect('customers:profile')
        else:
            err = "thong tin dang nhap khong dung"
    return render(request, 'customers/dang_nhap.html', {'err': err})

def profile(request):
    profile = Customer.objects.get(ho_ten=request.session['username'])
    if request.session.has_key('username'):
        username = request.session['username']
        return render(request, 'customers/profile.html', {'username': username, 'profile': profile, 'title': 'Thông tin khách hàng'})
    else:
        return redirect('customers:dang_nhap')

def dang_xuat(request):
    if request.session.has_key('username'):
        del request.session['username']
    return redirect('customers:dang_nhap')