from django.conf import settings
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect

from . import forms

def logout_user(request):
    logout(request)
    return redirect('login')
    
def login_page(request):
    form = forms.LoginForm()
    message =''
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username = form.cleaned_data['username'],
                password = form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                return redirect('home')
        message = 'Identifiants invalides.'
    return render(request, 'authentication/login.html', context={'form': form, 'message': message})


def signup_page(request):
    form = forms.SignupForm()
    if request.method == 'POST':
        form = forms.SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            # auto-login user
            login(request, user)
            return redirect(settings.LOGIN_REDIRECT_URL)
    return render(request, 'authentication/signup.html', context={'form': form})


def upload_profile_photo(request):
    form = forms.UploadProfilePhotoForm()

    if request.method == 'POST':
        form = forms.UploadProfilePhotoForm(request.POST, request.FILES ,instance= request.user)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'blog/photo_upload.html', context={'form': form})

