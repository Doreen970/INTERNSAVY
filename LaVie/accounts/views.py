from django.shortcuts import render, redirect
from .forms import SignupForm

# Create your views here.
"""
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')  # Redirect to the home page after registration
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')  # Redirect to the home page after login
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form}) 
    """

def user_logout(request):
    logout(request)
    return redirect('index') 
     
def signup(request):
    form = SignupForm()
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('/login')
        
        else:
            form = SignupForm()
    return render(request, "accounts/signup.html", {
        "form": form
    })         

        
