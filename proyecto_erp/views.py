from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages

@login_required
def dashboard(request):
    return render(request, 'dashboard.html', {
        'title': 'Panel de Control',
    })

@login_required
def profile(request):
    return render(request, 'perfil/profile.html')
