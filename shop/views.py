from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Whisky


def home(request):
    return render(request, 'shop/home.html')

class ProductListView(ListView):
    model = Whisky
    template_name = 'shop/whisky_home.html'
    context_object_name = 'products'
    ordering = ['-date_posted']
    paginate_by = 30;

class ProductDetailView(DetailView):
    model = Whisky
    template_name = "shop/product_detail.html"
    context_object_name = 'product'

class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Whisky
    fields = ['img', 'name', 'price', 'strength', 'size', 'type', 'distillery', 'bottler', 'casktype', 'casknumber',
              'vintage', 'serie', 'bottled', 'bottled', 'age', 'bottles_in_serie']
    template_name = 'shop/product_create.html'

    def form_valid(self, form):
        form.instance.seller = self.request.user
        return super().form_valid(form)

class ProductUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Whisky
    fields = ['img', 'name', 'price', 'strength', 'size', 'type', 'distillery', 'bottler', 'casktype', 'casknumber',
              'vintage', 'serie', 'bottled', 'bottled', 'age', 'bottles_in_serie']
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
    model = Whisky
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
