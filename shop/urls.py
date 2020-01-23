from django.urls import path

from . import views


urlpatterns = [
    path('', views.ProductListView.as_view(), name='shop-home'),
    path('about/', views.about, name='shop-about'),
]
