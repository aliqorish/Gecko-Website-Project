from django.urls import path
from . import views

urlpatterns = [
    path("",views.home,name="Home"),
    path("plan/",views.plan,name="plan"),
    path("edit/",views.edit,name="edit"),
    path("today/",views.today,name="today"),
    #path("home/",views.home,name="Home"),
]
