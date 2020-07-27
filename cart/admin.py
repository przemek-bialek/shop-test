from django.contrib import admin

from .models import Cart, CartItem, ShippingAddress


admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(ShippingAddress)
