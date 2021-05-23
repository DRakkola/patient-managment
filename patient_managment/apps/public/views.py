from django.shortcuts import render
from django.http import HttpRequest,HttpResponse
from patient_managment.apps.accounts.models import Patient

def index(request: HttpRequest) -> HttpResponse:
    print(request.POST)
    return render(request, "index.html")
    # template = loader.get_template('index.html')
    # return HttpResponse(template.render({}, request))


def patients(request: HttpRequest) -> HttpResponse:
    data = Patient.objects.all()
    context = {"Patient_number" : data}
    print(request.POST)
    return render(request, "patients.html",context)


def dashboard(request: HttpRequest) -> HttpResponse:
    print(request.POST)
    return render(request, "dashboard.html")

