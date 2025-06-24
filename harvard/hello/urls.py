from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:name>", views.greet,name="greet"),
    path("brain", views.brain, name="brain"),
    path("david", views.devid,name="david"),
]
