from django import forms
from customers.models import Customer

class FormSignin():
    user_name = forms.CharField(max_length = 50)
    mat_khau = forms.CharField(max_length = 50)

class CustomerCreate(forms.ModelForm):
    ho_ten = forms.CharField(max_length = 264)
    user_name = forms.CharField(max_length = 50)
    mat_khau = forms.CharField(widget = forms.PasswordInput())
    confirm = forms.CharField(widget = forms.PasswordInput())
    phone = forms.CharField(max_length = 15)
    email = forms.EmailField()
    dia_chi = forms.CharField(max_length = 200)
    class Meta:
        model = Customer
        fields = ['ho_ten', 'user_name', 'email','mat_khau','phone','dia_chi']