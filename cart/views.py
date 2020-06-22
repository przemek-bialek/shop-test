from django.contrib import messages
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from shop.models import Product
from .models import CartItem, Cart

class CartListView(LoginRequiredMixin, ListView):
    template_name = 'cart/cart.html'
    context_object_name = 'items'
    paginate_by = 10

    def get_queryset(self):
        return CartItem.objects.filter(cart__buyer=self.request.user)

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if data['items']:
            data['cart_price'] = data['items'][0].cart.cart_price
        return data

@login_required
def add_to_cart(request, product_slug):
    cart, created = Cart.objects.get_or_create(buyer=request.user, checked_out=False)
    product = get_object_or_404(Product, slug=product_slug)
    if CartItem.objects.filter(product=product, cart=cart).exists():
        messages.info(request, 'This item is already in your cart')
        return redirect('cart-view')
    item = CartItem.objects.create(product=product, cart=cart)
    cart.cart_price += item.total_price
    cart.save()
    item.save()
    messages.success(request, 'Item added to cart')
    return redirect('cart-view')

@login_required
def remove_from_cart(request, product_slug):
    #cart = get_object_or_404(Cart, buyer=request.user, checked_out=False)
    #product = get_object_or_404(Product, slug=product_slug)
    #item = get_object_or_404(CartItem, product=product, cart=cart)
    cart = Cart.objects.filter(buyer=request.user, checked_out=False)[0]
    product = get_object_or_404(Product, slug=product_slug)
    item = CartItem.objects.filter(product=product, cart=cart)
    if item:
        cart.cart_price -= item[0].total_price
        cart.save()
        item[0].delete()
        messages.success(request, 'Item removed from cart')
    else:
        messages.info(request, 'Item was not in your cart')
    return redirect('cart-view')
