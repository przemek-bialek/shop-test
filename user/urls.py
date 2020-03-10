from django.urls import path
from django.contrib.auth import views as auth_views

from . import views


urlpatterns = [
    path('register/', views.register, name='user-register'),
    path('login/', auth_views.LoginView.as_view(template_name='user/login.html'), name='user-login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='user/logout.html'), name='user-logout'),
    path('my_profile/', views.my_profile, name="user-my_profile"),
    path('profile/<str:username>/', views.profile, name='user-profile'),
    path('profile/<str:username>/<str:tabname>/', views.profile, name='user-profile_tabs'),
    path('rate/<str:rated_username>/', views.rate, name='user-rate'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='user/password_reset.html'), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='user/password_reset_done.html'), name='password_reset_done'),
    path('password_reset/confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='user/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password_reset/complete/', auth_views.PasswordResetCompleteView.as_view(template_name='user/password_reset_complete.html'), name='password_reset_complete'),
]
