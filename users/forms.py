from django import forms
from users.models import UserProfileInfo, User

class UserForm(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput())
    class Meta():
        model = User
        fields = ('first_name','last_name','username', 'email', 'password')

class UserProfileInfoForm(forms.ModelForm):
    porfolio = forms.URLField(required = False)
    picture = forms.ImageField(required = False)
    class Meta():
        model = UserProfileInfo
        fields = ('portfolio','picture')