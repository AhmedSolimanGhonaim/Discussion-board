from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth import login, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import SignUpForm, ProfileUpdateForm

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'accounts/signup.html', {'form': form})

@login_required
def my_profile(request):
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            messages.success(request, '<i class="fas fa-check-circle"></i> Your profile has been successfully updated!')
            return redirect('my_profile')
        else:
            messages.error(request, '<i class="fas fa-exclamation-circle"></i> Please correct the errors below.')
    else:
        form = ProfileUpdateForm(instance=request.user.profile)
    
    return render(request, 'accounts/my_profile.html', {'form': form})

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, '<i class="fas fa-check-circle"></i> Your password was successfully updated!')
            return redirect('my_profile')
        else:
            messages.error(request, '<i class="fas fa-exclamation-circle"></i> Please correct the errors below.')
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request, 'accounts/change_password.html', {'form': form})



