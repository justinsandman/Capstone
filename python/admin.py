# Authors:
#
# Description: This file is used to register the 
# database models to be managed through Django's 
# admin interface.
# 
# References: 

from django.contrib import admin 
from .models import User, ActivityLog, NutritionLog, LifestyleLog, Goal, BugTracking, SystemLog

# Register models so they appear in Django admin panel 
@admin.resgister(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'activity_level', 'account_created_date')
    search_fields = ('first_name', 'last_name', 'email')

@admin.register(ActivityLog)
class ActivityLogAdmin(admin.ModelAdmin):
    list_display = ('user', 'activity_type', 'duration', 'calories_burned', 'date_logged')
    list_filter = ('activity_type',)

@admin.register(NutritionLog)
class NutritionLogAdmin(admin.ModelAdmin):
    list_display = ('user', 'food_item', 'calories', 'proteins', 'carbs', 'fats', 'date_logged')
    search_fields = ('food_item',)

@admin.register(LifestyleLog)
class LifeStyleLog(admin.ModelAdmin):
    list_display = ('user', 'log_type', 'value', 'date_logged')
    list_filter = ('log_type',)

@admin.register(Goal)
class GoalAdmin(admin.ModelAdmin):
    list_display = ('user', 'goal_type', 'target_value', 'current_value', 'deadline')
    list_filter = ('goal_type',)

@admin.register(BugTracking)
class BugTrackingAdmin(admin.ModelAdmin):
    list_display = ('reported_by', 'description', 'severity', 'status', 'date_reported', 'date_resolved')
    list_filter = ('severity', 'status')

@admin.register(SystemLog)
class SystemLogAdmin(admin.ModelAdmin):
    list_display = ('event', 'event_date', 'details')
    list_filter = ('event_type',)

# May need to register more models if new tables created. 