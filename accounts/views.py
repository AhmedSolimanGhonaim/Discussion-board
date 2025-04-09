from django.shortcuts import render , redirect
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth import login, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import SignUpForm

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request , user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'accounts/signup.html', {'form': form})

@login_required
def my_profile(request):
    return render(request, 'accounts/my_profile.html')

@login_required
def change_password(request):
    # if request.method == 'POST':
    #     form = PasswordChangeForm(user=request.user, data=request.POST)
    #     if form.is_valid():
    #         user = form.save()
    #         update_session_auth_hash(request, user)
    #         messages.success(request, 'Your password was successfully updated!')
    #         return redirect('my_profile')
    # else:
    #     form = PasswordChangeForm(user=request.user)
    return render(request, 'accounts/change_password.html', {})



