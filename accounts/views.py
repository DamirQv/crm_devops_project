from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

def register_view(request):
    form = UserCreationForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        user = form.save()
        login(request, user)
        return redirect('/')
    return render(request, 'register.html', {'form': form})

def login_view(request):
    form = AuthenticationForm(request, data=request.POST or None)
    if request.method == 'POST' and form.is_valid():
        user = form.get_user()
        login(request, user)
        return redirect('/')
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('/login/')