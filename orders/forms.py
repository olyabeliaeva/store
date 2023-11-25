from django import forms

from orders.models import Order


class OrderForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Иван'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Пупянтик'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'you@example.com'}))
    adress = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control', 'placeholder': 'Беларусь, Минск, ул. Космонавтов, дом 23 к.1',
    }))

    class Meta:
        model = Order
        fields = ('first_name', 'last_name', 'email', 'adress')
