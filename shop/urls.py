from django.urls import path

from . import views


urlpatterns = [
    path('', views.ProductListView.as_view(), name='shop-home'),
    path('product/<slug:slug>/', views.ProductDetailView.as_view(), name='shop-product_detail'),
    path('about/', views.about, name='shop-about'),
]
