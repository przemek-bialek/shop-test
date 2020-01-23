from django.shortcuts import render
from django.views.generic import ListView

from .models import Product


class ProductListView(ListView):
    model = Product
    template_name = 'shop/home.html'
    context_object_name = 'products'
    ordering = ['-date_posted']

def about(request):
    return render(request, 'shop/about.html', {'title': 'About'})
