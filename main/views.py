from django.shortcuts import render, redirect, get_object_or_404
from .models import Day, Workout
from django.contrib.auth.decorators import login_required
from .forms import addW
from datetime import date

# Create your views here.
def home(response):
   return render(response, "home.html")

@login_required
def plan(response):
   d = Day.objects.filter(user=response.user)
   #print(d)
   do = [choice[0] for choice in Day.daysofweek.choices]
   d = sorted(d, key=lambda d: do.index(d.day))
   #print( d)
   #print(d[0].day)
   #print(d[0].todo)
   return render(response, "plan.html",{"days":d})

@login_required
def edit(response):
   if response.method == "POST":
        if "delete_workout" in response.POST:
            workout_id = response.POST.get("workout_id")
            workout = get_object_or_404(Workout, id=workout_id, tday__user=response.user)
            workout.delete()
            return redirect("edit")

        day_id = response.POST.get("day_id")
        d = get_object_or_404(Day, id=day_id, user=response.user)

        if "save_todo" in response.POST:
            d.todo = response.POST.get("todo", d.todo)
            d.save()

        elif "save_workout" in response.POST:
            form = addW(response.POST)
            if form.is_valid():
                workout = form.save(commit=False)
                workout.tday = d
                workout.save()

        return redirect("edit")   
   form = addW()
   d = Day.objects.filter(user=response.user)
   do = [choice[0] for choice in Day.daysofweek.choices]
   d = sorted(d, key=lambda d: do.index(d.day))
   return render(response, "edit.html",{"days":d,"form":form} )

weekdaynum = {
        0: "MON",
        1: "TUE",
        2: "WED",
        3: "THU",
        4: "FRI",
        5: "SAT",
        6: "SUN",
    }

@login_required
def today(response):
    todayc = weekdaynum[date.today().weekday()]
    d = get_object_or_404(Day, user=response.user, day=todayc)
    return render(response,"today.html",{"d":d, "todayd":date.today()})