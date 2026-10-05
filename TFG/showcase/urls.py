"""URL configuration for the showcase app."""

from django.urls import path

from . import views

urlpatterns = [
    path('', views.showcase),
]