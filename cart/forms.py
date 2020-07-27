from django import forms

from .models import ShippingAddress


PAYMENT_CHOICES = [
    ('P', 'PayPal'),
    ('T', 'Transfer'),
    ('C', 'Card'),
]

SHIPPING_CHOICES = [
    ('C', 'Courier'),
    ('P', 'Personal collection'),
]

class CheckoutForm(forms.Form):
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(CheckoutForm, self).__init__(*args, **kwargs)
        self.fields['address'].queryset = ShippingAddress.objects.filter(user=self.user)

    address = forms.ModelChoiceField(queryset=ShippingAddress.objects.all())
    payment_option = forms.ChoiceField(choices=PAYMENT_CHOICES)
    delivery_option = forms.ChoiceField(choices=SHIPPING_CHOICES)
