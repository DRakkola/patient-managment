#from django.http import HttpResponse
#from django.template import loader
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')
    #template = loader.get_template('index.html')
    # return HttpResponse(template.render({}, request))


def patients(request):
    return render(request, 'patients.html')


def dashboard(request):
    return render(request, 'dashboard.html')
