"""
Views for handling user authentication, navigation, and feature page rendering. 

Authors: Justin Sandstedt, Matthew Swandal, Gabriel Morgan

This module connects frontend templates with backend logic. It handles:
- Signup & Login workflows
- Route-based template rednering for feature pages
- Retrieval and submission of form data
"""
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages 
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_protect

from core.forms import SignupForm, FoodLogForm
from nutrition.models import FoodLog



def signup_view(request):
    """
    Handle user registration.

    If the request method is POST, validate and create a new user using SignupForm.
    Automatically logs in the new user and redirects to the dashboard. 
    If GET, renders blank SignupForm. 
    """
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



def login_view(request):
    """
    Handle user login. 

    Authenticated user credentials submitted via POST.
    Redirects to main dashboard on success or returns to login page with error on fail. 
    """
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')  # Redirect to the dashboard after login
        else:
            messages.error(request, "Invalid username or password")  # Display error message
            return redirect('login')  

    return render(request, 'login.html')



def settings(request):
    """
    Renders the settings page.
    """
    return render(request, 'Settings.html')



@csrf_protect
def food_log_view(request):
    """
    Render the FoodLog page. 
    TODO: Implement form submission. 
    """
    return render(request, 'foodlog.html')



def weight_log(request):
    """
    Render the WeightLog page.
    """
    return render(request, 'weightlog.html')



def habit_tracker(request):
    """
    Render the HabitTracker page. 
    """
    return render (request, 'HabitTracker.html')


def program(request):
    """
    Render the Program page. 
    """
    return render(request, 'program.html')



def expenditure(request):
    """
    Render the Expenditure page. 
    """
    return render(request, 'expenditure.html')



def sleep_log(request):
    """
    Render the SleepLog page. 
    """    
    return render(request, 'sleeplog.html')


def journal(request):
    """
    Render the Journal page. 
    """
    return render(request, 'journal.html')



def dashboard(request):
    """
    Render the MainDashboard page. 
    """
    return render(request, 'MainDashboard.html')

def my_account_view(request):
    """
    """
    context = {} 
    return render(request, 'MyAccount.html', context) 

def activity_level_view(request):
    """
    """
    context = {} 
    return render(request, 'ActivityLevel.html', context) 

def forgot_password_view(request):
    """
    """
    return render(request, "ForgotPassword.html")
