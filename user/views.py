from django.views import View
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from shop.models import Whisky
from .models import User, UserRating
from .forms import UserRegisterForm, UserUpdateForm, UserRatingCreateForm


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account has been successfully created. You can now login using those credentials')
            return redirect('user-login')
    else:
        form = UserRegisterForm()
    context = {
        'form': form
    }
    return render(request, 'user/register.html', context)

@login_required
def my_profile(request):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile data has been updated successfully')
            return redirect('user-profile')
    else:
        form = UserUpdateForm(instance=request.user)
    context = {
        'form': form
    }
    return render(request, 'user/my_profile.html', context)

def profile(request, username, tabname='products'):
    if request.method == 'GET':
        context = {}
        context['User'] = User.objects.get(username=username)
        if tabname == 'products':
            context['products'] = Whisky.objects.filter(seller=context['User'])
        elif tabname == 'ratings':
            context['ratings'] = UserRating.objects.filter(rated=context['User']);
            return render(request, 'user/profile_ratings.html', context)
    return render(request, 'user/profile.html', context)

@login_required
def rate(request, rated_username):
    rater_username = request.user.username
    print(request.method)
    if request.method == 'POST' and rater != rated:
        form = UserRatingCreateForm(request.POST)
        form.instance.rater = request.user
        form.instance.rated = User.objects.get(username=rated_username)
        print(form.instance.rater)
        print(form.instance.rated)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your rating has been successfully placed')
            return redirect('/')
    else:
        form = UserRatingCreateForm()
    context = {}
    context['form'] = form
    return render(request, 'user/rate.html', context)
