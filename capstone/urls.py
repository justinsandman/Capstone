# Authors: Justin Sandstedt, Matthew Swandal, Gabriel Morgan
#
# URLs for navigating various pages in the app.

from django.contrib import admin 
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.signup_view, name='signup'),  # Homepage or signup page
    path('login/', views.login_view, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('foodlog/', views.food_log, name='food_log'),
    path('expenditure/', views.expenditure, name='expenditure'),
    path('weightlog/', views.weight_log, name='weight_log'),
    path('habittracker/', views.habit_tracker, name='habit_tracker'),
    path('program/', views.program, name='program'),
    path('sleeplog/', views.sleep_log, name='sleep_log'),
    path('journal/', views.journal, name='journal'),
    path('settings/', views.settings, name='settings'),
]

