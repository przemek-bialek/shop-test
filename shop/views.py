from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView

from .models import Product
from .forms import ProductForm


class ProductListView(ListView):
    model = Product
    template_name = 'shop/home.html'
    context_object_name = 'products'
    ordering = ['-date_posted']

class ProductDetailView(DetailView):
    model = Product
    template_name = "shop/product_detail.html"
    context_object_name = 'product'

class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    #form_class = ProductForm
    fields = ['img', 'name', 'price']

    def form_valid(self, form):
        form.instance.seller = self.request.user
        return super().form_valid(form)

    #def get_success_url(self):
    #    return reverse('shop-product_detail', kwargs={'slug': self.model.slug})

    #def post(self, request, *args, **kwargs):
    #    form = self.form_class(request.POST, request.FILES)
    #    if form.is_valid():
    #        print('fprma jest se validnieta')
    #        form.save()
    #        print("ddddddduuuuuuuuuuupppppppppaaaaaaaaaaa")
    #        return redirect(self.success_url)
    #    else:
    #        return render(request, self.template_name, {'form': form})

def about(request):
    return render(request, 'shop/about.html', {'title': 'About'})
