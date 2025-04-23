"""
Admin interface configuration for ...

Authors: Justin Sandstedt, Matthew Swandal, Gabriel Morgan

This module registers custom admin views for the database models 
so they can be managed via Django's built-in admin panel. 

Each model is customized with:
- Fields to display in the admin list view
- Filters and search fields where relevant 
"""



from django.contrib import admin 
from nutrition.models import User, ActivityLog, FoodLog, LifestyleLog, Goal, BugTracking, SystemLog

# Activity model admin config
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'activity_level', 'date_joined')
    search_fields = ('first_name', 'last_name', 'email')



# ActivityLog model admin configuration
@admin.register(ActivityLog)
class ActivityLogAdmin(admin.ModelAdmin):
    list_display = ('user', 'activity_type', 'duration', 'calories_burned', 'date_logged')
    list_filter = ('activity_type',)



# FoodLog model admin configuration
@admin.register(FoodLog)
class FoodLogAdmin(admin.ModelAdmin):
    list_display = ('user', 'food_item', 'calories', 'proteins', 'carbs', 'fats', 'date_logged')
    search_fields = ('food_item',)



# LifeStyle model admin configuration
@admin.register(LifestyleLog)
class LifeStyleLog(admin.ModelAdmin):
    list_display = ('user', 'log_type', 'value', 'date_logged')
    list_filter = ('log_type',)



# GoalAdmin model admin configuration
@admin.register(Goal)
class GoalAdmin(admin.ModelAdmin):
    list_display = ('user', 'goal_type', 'target_value', 'current_value', 'deadline')
    list_filter = ('goal_type',)



# BugTracking model admin configuration
@admin.register(BugTracking)
class BugTrackingAdmin(admin.ModelAdmin):
    list_display = ('reported_by', 'description', 'severity', 'status', 'date_reported', 'date_resolved')
    list_filter = ('severity', 'status')



# SystemLog model admin configuration
@admin.register(SystemLog)
class SystemLogAdmin(admin.ModelAdmin):
    list_display = ('event_type', 'event_date', 'details')
    list_filter = ('event_type',)

# Note: Additional models should be registered here as they are created.
