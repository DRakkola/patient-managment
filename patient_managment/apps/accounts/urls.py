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
    path("login", views.loginPage, name="login"),
    path("register",views.register, name="register"),
    path("patient_form", views.patient_form, name="patient_form"),
]