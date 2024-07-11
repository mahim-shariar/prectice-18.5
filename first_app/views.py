from django.shortcuts import render, redirect
from django.contrib import messages
from . import forms
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm, SetPasswordForm
from django.contrib.auth import authenticate, login, logout,update_session_auth_hash
from django.contrib.auth.decorators import login_required

# Create your views here.


def register(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            register_forms = forms.registerForm(request.POST)
            if register_forms.is_valid():
                register_forms.save()
                messages.success(request, "Account Created Successfully")
                return redirect('profile')
        else:
            register_forms = forms.registerForm(request.POST)
        return render(request, 'register.html', {'form': register_forms, 'type': 'Register'})
    else:
        return redirect('profile')


def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = AuthenticationForm(request, request.POST)
            if form.is_valid():
                user_name = form.cleaned_data['username']
                user_pass = form.cleaned_data['password']
                user = authenticate(username=user_name, password=user_pass)
                if user is not None:
                    messages.success(request, "Logged in Successfully")
                    login(request, user)
                    return redirect('profile')
                else:
                    messages.warning(request, "Login information inorrect")
                    return redirect('register')
        else:
            form = AuthenticationForm()
        return render(request, 'register.html', {'form': form, 'type': 'Login'})
    else:
        return redirect('profile')


@login_required
def profile(request):
    return render(request, 'profile.html')



@login_required
def logout_view(request):
    logout(request)
    messages.success(request, "Logged out Successfully")
    return redirect('home')


@login_required
def pass_change(request):
    if request.method == 'POST':
        pass_change_form = PasswordChangeForm(request.user, request.POST)
        if pass_change_form.is_valid():
            user = pass_change_form.save()
            update_session_auth_hash(request, user)
            messages.success(request, "Password Changed Successfully")
            return redirect('profile')
    else:
        pass_change_form = PasswordChangeForm(request.user)
    return render(request, 'pass_change.html', {'form': pass_change_form})

@login_required
def set_password(request):
    if request.method == 'POST':
        set_password_form = SetPasswordForm(request.user, request.POST)
        if set_password_form.is_valid():
            user = set_password_form.save()
            update_session_auth_hash(request, user)
            messages.success(request, "Password Changed Successfully")
            return redirect('profile')
    else:
        set_password_form = SetPasswordForm(request.user)
    return render(request, 'pass_change.html', {'form': set_password_form})