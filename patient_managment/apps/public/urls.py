
from django.urls import path

from . import views

app_name = "public"
urlpatterns = [
    path("", views.index, name="index"),
    path("patients", views.patients, name="patients"),
    path("dashboard", views.dashboard, name="dashboard"),
    ]