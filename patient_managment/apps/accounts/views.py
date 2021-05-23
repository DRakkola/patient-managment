from patient_managment.apps.public.views import patients
from django.core.checks import messages
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest, HttpResponse
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .forms import registerform
from .models import Patient, Phone 
from django.contrib.auth.decorators import login_required

class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = "accounts/profile.html"
    

    

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('public:index')
    context = {}
    return render(request, 'accounts/login.html',context)
    
@login_required
def register(request):
        message = ''  
        if request.method == 'POST':
            name = request.POST.get('name')
            age = request.POST.get('age')
            phone = request.POST.getlist('tell')
            sex = request.POST.get('genre')
            grade = request.POST.get('grade')
            mlle = request.POST.get('mlle')
            profession = request.POST.get('profession')
            family_stats = request.POST.get('family_stats')
            hospital_service = request.POST.get('hospital_service')
            adresse = request.POST.get('adresse')
            ins = Patient(name=name , age=age, sex=sex, grade=grade, profession=profession, mlle=mlle, family_stats=family_stats, hospital_service=hospital_service, adresse=adresse)
            ins.save()
            new = Patient.objects.get(id=ins.pk)
            print(phone)
            for item in phone:
                ins = Phone(number=item,patientid=new)
                ins.save()
            message = 'Patient added succesufly ....!'
            context = { 'msg' : message }
            return render(request, "accounts/register.html")
        else:
            context = {}
            return render(request, 'accounts/register.html', context)

@login_required
def patient_form(request: HttpRequest) -> HttpResponse:
    return render(request, "accounts/patient_form.html")
