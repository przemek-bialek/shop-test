from django.urls import path

from . import views


urlpatterns = [
    path('', views.home, name='shop-home'),
    path('about/', views.about, name='shop-about'),
    path('<str:product_type>/sell/', views.ProductCreateView.as_view(), name='shop-product_create'),
    path('<str:product_type>/<slug:slug>/', views.ProductDetailView.as_view(), name='shop-product_detail'),
    path('<str:product_type>/', views.ProductListView.as_view(), name='shop-product_home'),
    path('<str:product_type>/<slug:slug>/update/', views.ProductUpdateView.as_view(), name='shop-product_update'),
    path('<str:product_type>/<slug:slug>/delete/', views.ProductDeleteView.as_view(), name='shop-product_delete'),
]
