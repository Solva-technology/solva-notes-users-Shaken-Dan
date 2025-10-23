from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from .forms import CustomUserCreationForm

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            authenticated_user = authenticate(request, username=username, password=raw_password)
            if authenticated_user is not None:
                auth_login(request, authenticated_user)
            return redirect("notes:home")
    else:
        form = CustomUserCreationForm()
    return render(request, "registration/register.html", {"form": form})
