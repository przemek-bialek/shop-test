from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Whisky, Metal
from .forms import WhiskyForm, MetalForm


def home(request):
    return render(request, 'shop/home.html')

class ProductListView(ListView):
    model = Whisky
    template_name = 'shop/product_list.html'
    context_object_name = 'products'
    ordering = ['-date_posted']
    paginate_by = 30;

    def get_queryset(self):
        MY_QUERYSETS = {
            'Whisky': Whisky.objects.all(),
            'Metal': Metal.objects.all(),
        }
        return MY_QUERYSETS[self.kwargs['product_type']]

class ProductDetailView(DetailView):
    template_name = "shop/product_detail.html"
    context_object_name = 'product'

    def get_queryset(self):
        MY_QUERYSETS = {
            'Whisky': Whisky.objects.filter(slug=self.kwargs['slug']),
            'Metal': Metal.objects.filter(slug=self.kwargs['slug']),
        }
        return MY_QUERYSETS[self.kwargs['product_type']]

class ProductCreateView(LoginRequiredMixin, CreateView):
    template_name = 'shop/product_create.html'

    def get_form_class(self):
        MY_FORMS = {
            'Whisky': WhiskyForm,
            'Metal': MetalForm,
        }
        return MY_FORMS[self.kwargs['product_type']]

    def get_success_url(self):
        return f'/{self.kwargs["product_type"]}/{self.object.slug}/'

    def form_valid(self, form):
        form.instance.seller = self.request.user
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    template_name = 'shop/product_update.html'

    def get_queryset(self):
        if self.kwargs['product_type'] == 'Whisky':
            return Whisky.objects.filter(slug=self.kwargs['slug'])
        elif self.kwargs['product_type'] == 'Metal':
            return Metal.objects.filter(slug=self.kwargs['slug'])
        else:
            return []

    def get_form_class(self):
        MY_FORMS = {
            'Whisky': WhiskyForm,
            'Metal': MetalForm,
        }
        return MY_FORMS[self.kwargs['product_type']]

    def get_success_url(self):
        return f'/{self.kwargs["product_type"]}/{self.object.slug}/'

    def form_valid(self, form):
        form.instance.seller = self.request.user
        return super().form_valid(form)

    def test_func(self):
        product = self.get_object()
        if self.request.user == product.seller:
            return True
        return False

class ProductDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    template_name = 'shop/product_delete.html'
    context_object_name = 'product'
    success_url = '/'

    def get_queryset(self):
        if self.kwargs['product_type'] == 'Whisky':
            return Whisky.objects.filter(slug=self.kwargs['slug'])
        elif self.kwargs['product_type'] == 'Metal':
            return Metal.objects.filter(slug=self.kwargs['slug'])
        else:
            return []

    def test_func(self):
        product = self.get_object()
        if self.request.user == product.seller:
            return True
        return False

def about(request):
    return render(request, 'shop/about.html', {'title': 'About'})
