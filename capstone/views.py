# Authors: Justin Sandstedt, Matthew Swandal, Gabriel Morgan
#
# Python file to retrieve data from Cloud SQL DB, process user 
# input, render HTML templates with DB content, & handle certain logic.

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages 
from django.contrib.auth.models import User
from core.forms import SignupForm  

def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  
            return redirect('dashboard')  
        else:
            print("Form is invalid:", form.errors)  
    else:
        form = SignupForm()

    return render(request, 'signup.html', {'form': form})

#
#
#
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')  # Redirect to the dashboard after login
        else:
            messages.error(request, "Invalid username or password")  # Display error message
            return redirect('login')  # Stay on the login page

    return render(request, 'login.html')

#
#
#
def settings(request):
    return render(request, 'Settings.html')

def dashboard(request):
    return render(request, 'MainDashboard.html')

