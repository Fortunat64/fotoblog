from django.shortcuts import render
from django.contrib.auth import login, authenticate #import des fonction de login et d'authentification

from . import forms


def login_page(request):
    form = forms.LoginForm()
    message =''
    if request.method == 'POST':
        form = forms.LoginForm(request.Post)
        if form.is_valid():
            user = authenticate(
                username = form.cleaned_data['username'],
                password = form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                message = f'Bonjour, {user.username}! Vous êtes connecté.'
            else:
                message = 'Identifiants invalides.'
    return render(request, 'authentication/login.html', context={'form': form, 'message': message})
