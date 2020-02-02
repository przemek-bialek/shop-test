from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Product


class ProductListView(ListView):
    model = Product
    template_name = 'shop/home.html'
    context_object_name = 'products'
    ordering = ['-date_posted']
    paginate_by = 30;

class ProductDetailView(DetailView):
    model = Product
    template_name = "shop/product_detail.html"
    context_object_name = 'product'

class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    fields = ['img', 'name', 'price']
    template_name = 'shop/product_create.html'

    def form_valid(self, form):
        form.instance.seller = self.request.user
        return super().form_valid(form)

class ProductUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Product
    fields = ['img', 'name', 'price']
    template_name = 'shop/product_update.html'

    def form_valid(self, form):
        form.instance.seller = self.request.user
        return super().form_valid(form)

    def test_func(self):
        product = self.get_object()
        if self.request.user == product.seller:
            return True
        return False

class ProductDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Product
    template_name = 'shop/product_delete.html'
    context_object_name = 'product'
    success_url = '/'

    def test_func(self):
        product = self.get_object()
        if self.request.user == product.seller:
            return True
        return False

def about(request):
    return render(request, 'shop/about.html', {'title': 'About'})
