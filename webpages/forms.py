from django import forms
from webpages.models import Contact

class CreateContact(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email','phone','message']