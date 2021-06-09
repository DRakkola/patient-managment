from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib import admin

from . import views
app_name = "accounts"
urlpatterns = [
    path("accounts/profile", views.ProfileView.as_view(), name="profile"),
    # Django Auth
    #path(
    #    "login",
    #    auth_views.LoginView.as_view(template_name="accounts/login.html"),
    #    name="login",
    #),
    path("logout", auth_views.LogoutView.as_view(), name="logout"),
    path("patients", views.patients, name="patients"),
    path("login", views.loginPage, name="login"),
    path("register",views.register, name="register"),
    path("patients",views.patients, name="patients"),
    path("patient_profile", views.patient_profile, name="patient_profile"),
    path("dossier",views.dossier,name="dossier"),
    path("patient_form",views.patient_form,name="patient_form"),
    path("patient_media",views.media,name="patient_media")
]
