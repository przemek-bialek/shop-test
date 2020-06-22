from django.urls import path
from django.contrib.auth.decorators import login_required

from . import views


urlpatterns = [
    path('', login_required(views.CartListView.as_view()), name='cart-view'),
    path('add_to_cart/<slug:product_slug>', views.add_to_cart, name='add_to_cart-view'),
    path('remove_from_cart/<slug:product_slug>', views.remove_from_cart, name='remove_from_cart-view'),
]
