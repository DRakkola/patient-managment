from django.shortcuts import render
from django.http import HttpRequest,HttpResponse


def index(request: HttpRequest) -> HttpResponse:
    print(request.POST)
    return render(request, "index.html")
    # template = loader.get_template('index.html')
    # return HttpResponse(template.render({}, request))


def patients(request: HttpRequest) -> HttpResponse:
    print(request.POST)
    return render(request, "patients.html")


def dashboard(request: HttpRequest) -> HttpResponse:
    print(request.POST)
    return render(request, "dashboard.html")