from django.contrib import admin
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import path
from django.conf import settings

def home_page(request):
    return render(request, "templates/index.html")

urlpatterns = [
    path("", home_page, name="index"),
]

