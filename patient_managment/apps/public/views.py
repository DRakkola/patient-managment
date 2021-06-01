from django.shortcuts import render
from django.http import HttpRequest,HttpResponse,JsonResponse
from patient_managment.apps.accounts.models import Patient

def index(request: HttpRequest) -> HttpResponse:
    print(request.POST)
    return render(request, "index.html")
    # template = loader.get_template('index.html')
    # return HttpResponse(template.render({}, request))


def dashboard(request: HttpRequest) -> HttpResponse:
    print(request.POST)
    return render(request, "dashboard.html")

