# Authors: Justin Sandstedt, Matthew Swandal, Gabriel Morgan
#
# Python file to retrieve data from Cloud SQL DB, process user 
# input, render HTML templates with DB content, & handle certain logic.

from django.shortcuts import render, redirect 
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from nutrition.models import ActivityLog, NutritionLog
from ..python.utils import fetch_nutrition_data # Utility function to get food data 
from ..python.forms import SignupForm, LoginForm, FoodLogForm 

# Main Dashboard
def dashboard(request):
    return render(request, 'MainDashboard.html')

# Signup Page 
def signup(request):
    if request.method == 'POST':  
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')  # Redirect to a named URL, not an HTML file
    else:
        form = SignupForm()  # This should only be defined when method is GET
    return render(request, 'signup.html', {'form': form})

# Food Log Page 
@login_required
def food_log(request):
    if request.method == 'POST':
        form = FoodLogForm(request.POST)
        if form.is_valid():
            food_entry = form.save(commit=False)
            food_entry.user = request.user 
            food_entry.save()
            return redirect('food_log')  # Use named URL patterns
    else:
        form = FoodLogForm()  # This should only be defined for GET requests

    logs = NutritionLog.objects.filter(user=request.user).order_by('-date_logged')
    return render(request, 'foodlog.html', {'form': form, 'logs': logs})

# Fetch Food Nutrition Data
@login_required
def get_food_nutrition(request):  # Fixed typo
    food_name = request.GET.get('food')
    if food_name:
        try:
            data = fetch_nutrition_data(food_name)  # Calls API utility function
            return JsonResponse(data, safe=False)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)  # Handle API errors
    return JsonResponse({'error': 'No Food Specified'}, status=400)

# Activity Log Page 
@login_required
def activity_log(request):
    logs = ActivityLog.objects.filter(user=request.user).order_by('-date_logged')
    return render(request, 'ActivityLevel.html', {'logs': logs})
