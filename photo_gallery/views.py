from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import RegistrationForm, ProfileForm, UserUpdateForm
from .models import Profile


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Account created successfully! Welcome to Photo Gallery.')
            return redirect('home')
    else:
        form = RegistrationForm()

    return render(request, 'register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'Login successful! Welcome back.')
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password. Please try again.')
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')

def home(request):
    return render(request, 'home.html')


@login_required
def profile(request):
    user_profile = get_object_or_404(Profile, user=request.user)

    if request.method == 'POST':
        profile_form = ProfileForm(
            request.POST,
            request.FILES,
            instance=user_profile
        )

        user_form = UserUpdateForm(
            request.POST,
            instance=request.user
        )

        if profile_form.is_valid() and user_form.is_valid():
            profile_form.save()
            user_form.save()

            messages.success(request, 'Profile updated successfully!')
            return redirect('profile')

    else:
        profile_form = ProfileForm(instance=user_profile)
        user_form = UserUpdateForm(instance=request.user)

    return render(request, 'profile.html', {
        'profile_form': profile_form,
        'user_form': user_form,
        'profile': user_profile
    })