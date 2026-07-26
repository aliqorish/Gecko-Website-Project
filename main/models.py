from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Day(models.Model):
    class daysofweek(models.TextChoices):
        SATURDAY = "SAT", "Saturday",
        SUNDAY ="SUN", "Sunday",
        MONDAY = "MON", "Monday",
        TUESDAY = "TUE", "Tuesday",
        WEDNESDAY = "WED", "Wednesday",
        THURSDAY = "THU", "Thursday",
        FRIDAY = "FRI", "Friday"

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    day = models.CharField(max_length=3, choices=daysofweek.choices)
    todo = models.CharField(max_length=100, default= "Rest day")

    class Meta:
        unique_together = ("user", "day")
        ordering = ["user","day"]

class Workout(models.Model):
    tday = models.ForeignKey(Day, on_delete=models.CASCADE, related_name="workouts")
    name = models.CharField(max_length = 200)
    sets = models.IntegerField(blank=True, null=True)
    reps = models.IntegerField(blank=True, null=True)
    done = models.BooleanField(default = False)
