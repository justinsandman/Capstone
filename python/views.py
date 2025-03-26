# Authors: Justin Sandstedt, Matthew Swandal, Gabriel Morgan
#
# Python file to retrieve data from Cloud SQL DB, process user 
# input, render HTML templates with DB content, & handle certain logic.

from django.shortcuts import render, redirect 
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import FoodLog, ActivityLog, NutritionLog
from .utils import fetch_nutrition_data # Necessary utility function to get food data 
from .forms import SignupForm, LoginForm, FoodLogForm # Need to create file still!

# Main Dashboard
def dashboard(request):
    return render(request, 'MainDashboard.html')

# Signup Page 
def signup(request):
    if request.method == 'POST': # 
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('singnup.html')
        else:
            form = SignupForm()
        return render(request, 'signup.html', {'form': form})
    
# Food Log Page 
@login_required #
def food_log(request):
    if request.method == 'POST':
        form = FoodLogForm(request.POST)
        if form.is_valid():
            food_entry = form.save(commit=False)
            food_entry.user = request.user 
            food_entry.save()
            return redirect('food_log')
        else:
            form = FoodLogForm()
        logs = FoodLog.objects.filter(user=request.user).order_by('-date_logged')
        return render(request, 'foodlog.html', {'form': form, 'logs': logs})

@login_required
def get_food_nutriition(request):
    food_name = request.GET.get('food')
    if food_name:
        data = fetch_nutrition_data(food_name) # Calls API utility function
        return JsonResponse(data, safe=False)
    return JsonResponse({'error', 'No Food Specified'}, status=400) #

# Activity Log Page 
@login_required
def activity_log(request):
    logs = ActivityLog.objects.filter(user=request.user).order_by('-date_logged')
    return render(request, 'ActivityLevel.html', {'logs': logs})
