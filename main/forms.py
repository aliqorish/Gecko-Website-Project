from django import forms
from .models import Workout, Day
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class addW(forms.ModelForm):
    class Meta:
        model = Workout
        fields = ['name']
class DayForm(forms.ModelForm):
    class Meta:
        model = Day
        fields = ['todo']