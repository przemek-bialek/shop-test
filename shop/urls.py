from django.urls import path

from . import views


urlpatterns = [
    path('', views.home, name='shop-home'),
    path('whisky/', views.ProductListView.as_view(), name='shop-whisky_home'),
    path('about/', views.about, name='shop-about'),
    path('product/sell/', views.ProductCreateView.as_view(), name='shop-product_create'),
    path('product/<slug:slug>/', views.ProductDetailView.as_view(), name='shop-product_detail'),
    path('product/<slug:slug>/update/', views.ProductUpdateView.as_view(), name='shop-product_update'),
    path('product/<slug:slug>/delete/', views.ProductDeleteView.as_view(), name='shop-product_delete'),
]
