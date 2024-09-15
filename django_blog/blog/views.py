from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

# Login view
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('profile')  # Redirect to the profile page after login
    else:
        form = AuthenticationForm()
    return render(request, 'blog/login.html', {'form': form})

# Logout view
@login_required
def logout_view(request):
    logout(request)
    return redirect('login')  # Redirect to login page after logout

from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm

def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()  # Save the user to the database
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'blog/register.html', {'form': form})

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

@login_required
def profile(request):
    return render(request, 'blog/profile.html', {'user': request.user})

# Extend to allow profile editing
@login_required
def edit_profile(request):
    if request.method == "POST":
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserUpdateForm(instance=request.user)
    return render(request, 'blog/edit_profile.html', {'form': form})
