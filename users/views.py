from django.shortcuts import render
from users import models
from users import forms

# Create your views here.
def register(request):
    registered = False
    if request.method == "POST":
        form_user = forms.UserForm(data = request.POST)
        form_por = forms.UserProfileInfoForm(data = request.POST)
        if form_user.is_valid() and form_por.is_valid():
            user = form_user.save()
            user.set_password(user.password)
            user.save()

            profile = form_por.save(commit = False)
            profile.user = user
            
            print(request.FILES)
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']
            
            profile.save()
            registered = True
        else:
            print(form_user.errors, form_por.errors)
    else:
        form_user = forms.UserForm()
        form_por = forms.UserProfileInfoForm()
    return render(request, "users/registration.html", {'user_form':form_user,'profile_form': form_por, 'registered': registered})


def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password = password)
        if user.is_active:
            login(request, user)
            result = "Chào bạn " + username
            return render(request, "users/profile.html", {"result":result})
        else:
            print("Không đăng nhập được")
            print("Username: {} and password: {}".format(username, password))
            login_result = "Username và password không hợp lệ"
            return render(request, "users/login.html",{"login_result", login_result})
    else:
        return render(request, "users/login.html")


def user_logout(request):
    logout(request)
    result = "Bạn đã đăng xuất. Vui lòng chọn 'Đăng nhập'"
    return render(request, "users/profile.html", {"result":result})