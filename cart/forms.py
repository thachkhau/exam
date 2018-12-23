from django import forms

Quantity_choice = [(i, str(i)) for i in range(1, 10)]
class AddToCartForm(forms.Form):
    quantity = forms.TypedChoiceField(coerce= int, choices = Quantity_choice, label = 'Số lượng')
    update = forms.BooleanField(required = False, widget = forms.HiddenInput)