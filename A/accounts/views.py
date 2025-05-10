from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .forms import SignUpForm, LoginForm


def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'ثبت‌نام با موفقیت انجام شد! اکنون وارد شوید.')
            return redirect('accounts:login')
    else:
        form = SignUpForm()
    return render(request, 'accounts/signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form.cleaned_data['user']
            login(request, user)
            messages.success(request, 'با موفقیت وارد شدید.')
            return redirect('home:profile')
    else:
        form = LoginForm()
    return render(request, 'accounts/login.html', {'form': form})


def logout_view(request):
    logout(request)
    messages.info(request, 'خروج انجام شد.')
    return redirect('home:home')


@login_required(login_url='accounts:login')
def profile_view(request):
    # اینجا request.user همون کاربریه که الان لاگین کرده
    return render(request, 'accounts/profile.html', {'user': request.user})
