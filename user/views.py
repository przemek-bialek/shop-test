from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import UserRegisterForm


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account has been successfully created. You can now login using those credentials")
            return redirect('user-login')
    else:
        form = UserRegisterForm()
    context = {
        'form': form
    }
    return render(request, 'user/register.html', context)
