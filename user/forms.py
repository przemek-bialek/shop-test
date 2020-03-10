from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import User, UserRating


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('img', 'username', 'email')

class UserRatingCreateForm(forms.ModelForm):
    class Meta:
        model = UserRating
        fields = ('comment', )
