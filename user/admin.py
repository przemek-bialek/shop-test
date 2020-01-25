from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import UserRegisterForm, UserUpdateForm
from .models import User

class AdminUser(UserAdmin):
    add_form = UserRegisterForm
    form = UserUpdateForm
    model = User
    list_display = ['email', 'username',]

admin.site.register(User, AdminUser)
