from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib import admin
from .views import media
from django.conf import settings
from django.conf.urls.static import static

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
    path("pics_list",media.as_view(),name="pics_list"),
    path("add_image/",views.addpicsView.as_view(),name="add_image"),
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
