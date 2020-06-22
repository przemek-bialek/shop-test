from django import template

from cart.models import CartItem, Cart


register = template.Library()
@register.filter
def cart_count(user):
    cart = Cart.objects.filter(checked_out=False, buyer=user)
    if cart.exists():
        return CartItem.objects.filter(cart=cart[0]).count()
    return None
