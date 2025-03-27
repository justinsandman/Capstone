# Authors: Justin Sandstedt, Matthew Swandal, Gabriel Morgan
#
# 

from django.urls import path
from . import views  # Ensure views are correctly imported

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("signup/", views.signup, name="signup"),
    path("food_log/", views.food_log, name="food_log"),
    path("activity_log/", views.activity_log, name="activity_log"),
    path("get_food_nutrition/", views.get_food_nutrition, name="get_food_nutrition"),  # For fetching nutrition
]

