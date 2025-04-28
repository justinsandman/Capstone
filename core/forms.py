"""
Forms for user input & interaction.

Authors: Justin Sandstedt, Matthew Swandal, Gabriel Morgan

This file defines Django forms used for:
- User registiration 
- Logging food, weight, sleep, habits, programs, and journal entries
- Structuring HTML form rendering & validation

Forms are based on Django's built-in forms or custom-defined ones for apps needs. 
"""
from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from nutrition.models import FoodLog



# User signup form using Django's built-in UserCreationForm
class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']



# Form to log food consumption, connected to our FoodLog model
class FoodLogForm(forms.ModelForm):
    class Meta:
        model = FoodLog  # Link to the FoodLog model
        fields = ['user', 'food_item', 'calories', 'proteins', 'carbs', 'fats']



# Weight Logging form 
class WeightLogForm(forms.Form):
    weight = forms.FloatField(label = 'Weight (lbs)')
    date_logged = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))



# Simple Habit tracking form 
class HabitTracker(forms.Form):
    habit_name = forms.CharField(label = 'Habit Name', max_length=100)
    completed = forms.BooleanField(required=False)



# Program creation/tracking form
class ProgramForm(forms.Form):
    program_name = forms.CharField(label = 'Program Name', max_length=100)
    description = forms.CharField(widget=forms.Textarea)
    is_active = forms.BooleanField(required=False)



# Expenditure
# class ExpenditureForm(forms.Form):



# Sleep tracking form 
class SleepLogForm(forms.Form):
     hours_slept = forms.FloatField(label='Hours Slept')
     date_logged = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))



# Journal entry form 
class JournalForm(forms.Form): 
     title = forms.CharField(label='Title', max_length=100)
     content = forms.CharField(label='Content', widget=forms.Textarea)
     date_logged = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))