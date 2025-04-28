"""
Project URL Configuration

Authors: Justin Sandstedt, Matthew Swandal, Gabriel Morgan

This module defines the URL patterns for the main application. Each path
maps a specific route to a view function that handles the logic and rendering 
for that endpoint.

For more information, see: ... 
"""
from django.contrib import admin 
from django.urls import path, include
from . import views # Import local views 


urlpatterns = [

    # Sign up page - ... 
    path('', views.signup_view, name='signup'),  
    
    # Login route 
    path('login/', views.login_view, name='login'),

    # Main dashboard after Login
    path('dashboard/', views.dashboard, name='dashboard'),
    
    # Feature routes 
    path('foodlog/', views.food_log_view, name='food_log_view'),      #
    path('expenditure/', views.expenditure, name='expenditure'),      #
    path('weightlog/', views.weight_log, name='weight_log'),          #
    path('habittracker/', views.habit_tracker, name='habit_tracker'), #
    path('program/', views.program, name='program'),                  #
    path('sleeplog/', views.sleep_log, name='sleep_log'),             #
    path('journal/', views.journal, name='journal'),                  #
    path('settings/', views.settings, name='settings'),               #

    # Route for My Account page (accessible from settings)
    path('my-account/', views.my_account_view, name='my_account'),

    # Route for Activity Level page (accessible from settings)
    path('activity-level/', views.activity_level_view, name='activity_level'),

    path('forgot-password/', views.forgot_password_view, name='forgot_password'),
]

