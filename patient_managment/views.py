# from django.http import HttpResponse
# from django.template import loader
from django.shortcuts import render
from django.http import HttpRequest,HttpResponse
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


def index(request: HttpRequest) -> HttpResponse:
    return render(request, "index.html")
    # template = loader.get_template('index.html')
    # return HttpResponse(template.render({}, request))


def patients(request: HttpRequest) -> HttpResponse:
    return render(request, "patients.html")


def dashboard(request: HttpRequest) -> HttpResponse:
    return render(request, "dashboard.html")


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = "accounts/profile.html"
