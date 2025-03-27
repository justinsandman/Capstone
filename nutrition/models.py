# Authors: Justin Sandstedt, Matthew Swandal, Gabriel Morgan
#
# Python file where habits will be stored and tracked. 
# Will expand upon later. 

from django.db import models 
from django.contrib.auth.models import AbstractUser

# User model (Extends the already built-in Django User model)

class User(AbstractUser):
    ACTIVITY_LEVELS = [
        ('Sedentary', 'Sedentary'),
        ('Lightly Active', 'Lightly Active'),
        ('Active', 'Active'), 
        ('Very Active', 'Very Active'),
    ]

    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')])
    date_of_birth = models.DateField(null=True, blank=True)
    activity_level = models.CharField(max_length=20, choices=ACTIVITY_LEVELS, default='Sedentary')

    def __str__(self):
        return self.username # Django's built-in username field 

# Activity Log model (Tracks workouts)
class ActivityLog(models.Model):
    ACTIVITY_TYPES = [('Cardio', 'Cardio'), ('Strength', 'Strength'), ('Stretching', 'Stretching')]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    activity_type = models.CharField(max_length=20, choices=ACTIVITY_TYPES)
    duration = models.PositiveIntegerField(help_text="Duration in minutes")
    calories_burned = models.PositiveIntegerField()
    date_logged = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.activity_type} on {self.date_logged.date()}"

# Nutrition Log model (Tracks food intake)
class NutritionLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    food_item = models.CharField(max_length=255)
    calories = models.PositiveIntegerField()
    proteins = models.FloatField(help_text="Grams of protein")
    carbs = models.FloatField(help_text="Grams of carbohydrates")
    fats = models.FloatField(help_text="Grams of fat")
    date_logged = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.food_item} on {self.date_logged.date()}"

# Lifestyle Log model (Tracks sleep & water intake)
class LifestyleLog(models.Model):
    LOG_TYPES = [('Sleep', 'Sleep'), ('Water Intake', 'Water Intake')]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    log_type = models.CharField(max_length=50, choices=LOG_TYPES)
    value = models.CharField(max_length=50, help_text="Sleep hours or water intake in liters")
    date_logged = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.log_type}: {self.value} on {self.date_logged.date()}"

# Goal model (Tracks fitness goals)
class Goal(models.Model):
    GOAL_TYPES = [('Weight Loss', 'Weight Loss'), ('Muscle Gain', 'Muscle Gain'), ('Hydration', 'Hydration')]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    goal_type = models.CharField(max_length=50, choices=GOAL_TYPES)
    target_value = models.PositiveIntegerField()
    current_value = models.PositiveIntegerField(default=0)
    deadline = models.DateField()

    def __str__(self):
        return f"{self.user.username} - {self.goal_type} by {self.deadline}"

# Bug Tracking model (Tracks reported issues)
class BugTracking(models.Model):
    SEVERITY_LEVELS = [('Low', 'Low'), ('Medium', 'Medium'), ('High', 'High')]
    STATUS_CHOICES = [('New', 'New'), ('Assigned', 'Assigned'), ('Reproduced', 'Reproduced'),
                      ('Fixed', 'Fixed'), ('Tested', 'Tested'), ('Closed', 'Closed')]

    reported_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    description = models.TextField()
    severity = models.CharField(max_length=10, choices=SEVERITY_LEVELS)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='New')
    date_reported = models.DateTimeField(auto_now_add=True)
    date_resolved = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Bug {self.id} - {self.status}"

# System Log model (Tracks system events)
class SystemLog(models.Model):
    EVENT_TYPES = [('Performance Check', 'Performance Check'), ('Security Audit', 'Security Audit')]

    event_type = models.CharField(max_length=50, choices=EVENT_TYPES)
    event_date = models.DateTimeField(auto_now_add=True)
    details = models.TextField()

    def __str__(self):
        return f"{self.event_type} - {self.event_date}"
    
