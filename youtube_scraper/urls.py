from django.contrib import admin
from django.urls import path, include
from youtube_scraper import views

urlpatterns = [
    path('', views.index, name="index"),
]