from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import RegistrationForm, ProfileForm, UserUpdateForm, PhotoForm
from .models import Profile, Photo


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
    photos = Photo.objects.all().order_by('-created_at')

    tag = request.GET.get('tag', '').strip()

    print("SEARCHED TAG:", tag)

    if tag:
        photos = photos.filter(tags__icontains=tag)

    print("NUMBER OF PHOTOS:", photos.count())

    return render(request, 'home.html', {
        'photos': photos,
        'selected_tag': tag
    })

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


@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)

            messages.success(
                request,
                'Your password has been changed successfully!'
            )
            return redirect('profile')
    else:
        form = PasswordChangeForm(request.user)

    return render(request, 'change_password.html', {
        'form': form
    })


@login_required
def upload_photo(request):
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)

        if form.is_valid():
            photo = form.save(commit=False)
            photo.user = request.user
            photo.save()

            messages.success(request, 'Photo uploaded successfully!')
            return redirect('home')
    else:
        form = PhotoForm()

    return render(request, 'upload_photo.html', {
        'form': form
    })


def photo_detail(request, photo_id):
    photo = get_object_or_404(Photo, id=photo_id)

    return render(request, 'photo_detail.html', {
        'photo': photo
    })


@login_required
def photo_interaction(request, photo_id, action):
    photo = get_object_or_404(Photo, id=photo_id)

    if request.method == 'POST':

        if action == 'like':
            if request.user in photo.dislikes.all():
                photo.dislikes.remove(request.user)

            if request.user in photo.likes.all():
                photo.likes.remove(request.user)
            else:
                photo.likes.add(request.user)

        elif action == 'dislike':
            if request.user in photo.likes.all():
                photo.likes.remove(request.user)

            if request.user in photo.dislikes.all():
                photo.dislikes.remove(request.user)
            else:
                photo.dislikes.add(request.user)

    return redirect('photo_detail', photo_id=photo.id)