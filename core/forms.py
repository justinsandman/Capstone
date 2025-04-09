# Authors: Justin Sandstedt, Matthew Swandal, Gabriel Morgan
#
# 


from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from nutrition.models import NutritionLog

# User Signup Form
class SignupForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

# User Login Form
class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Username")
    password = forms.CharField(label="Password", widget=forms.PasswordInput)

# Food Log Form
class FoodLogForm(forms.ModelForm):
    class Meta:
        model = NutritionLog
        fields = ["food_item"] 


