from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.hello, name="index"),
    path("absent", views.absent),
    path("attendences", views.attendences),
    path("count", views.count_attendance),
    path("slip", views.slip)
]