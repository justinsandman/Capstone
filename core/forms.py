# Authors: Justin Sandstedt, Matthew Swandal, Gabriel Morgan
#
# 

from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from nutrition.models import FoodLog


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

class FoodLogForm(forms.ModelForm):
    class Meta:
        model = FoodLog  # Link to the FoodLog model
        fields = ['user', 'food_item', 'calories', 'proteins', 'carbs', 'fats']

# Weight Log
class WeightLogForm(forms.Form):
    weight = forms.FloatField(label = 'Weight (lbs)')
    date_logged = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

# Habit Tracker
class HabitTracker(forms.Form):
    habit_name = forms.CharField(label = 'Habit Name', max_length=100)
    completed = forms.BooleanField(required=False)

# Program Form
class ProgramForm(forms.Form):
    program_name = forms.CharField(label = 'Program Name', max_length=100)
    description = forms.CharField(widget=forms.Textarea)
    is_active = forms.BooleanField(required=False)

# Expenditure
# class ExpenditureForm(forms.Form):

# Sleep Log 
class SleepLogForm(forms.Form):
     hours_slept = forms.FloatField(label='Hours Slept')
     date_logged = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

# Journal
class JournalForm(forms.Form): 
     title = forms.CharField(label='Title', max_length=100)
     content = forms.CharField(label='Content', widget=forms.Textarea)
     date_logged = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
