# Authors: Justin Sandstedt, Matthew Swandal, Gabriel Morgan
#
# URLs for navigating various pages in the app.

from django.contrib import admin 
from django.urls import path, include
from . import views

urlpatterns = [


    path('dashboard/', views.dashboard, name='dashboard'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),

    path('', views.dashboard, name='dashboard'),  # Main dashboard
    path('settings/', views.settings, name='settings'),  # Settings page route

]
