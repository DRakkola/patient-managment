from django.core.checks import messages
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest, HttpResponse ,HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .forms import registerform
from .models import CardioVasculaire, Dossier, Form, Patient, Phone 
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

    if request.method == 'POST':
        card_1 = request.POST.get('card_1')
        card_2 = request.POST.get('card_2')
        card_3 = request.POST.get('card_3')
        card_4 = request.POST.get('card_4')
        card_5 = request.POST.get('card_5')
        card_6 = request.POST.get('card_6')
        card_7 = request.POST.get('card_7')
        card_8 = request.POST.get('card_8')
        card_9 = request.POST.get('card_9')
        card_10 = request.POST.get('card_10_in')
        card_11 = request.POST.get('card_11_in')
        card_12 = request.POST.get('card_12')
        card_13 = request.POST.get('card_13')
        card_14 = request.POST.get('card_14')
        card_15 = request.POST.get('card_15')
        card_16 = request.POST.get('card_16')
        card_17 = request.POST.get('card_17')
        card_18 = request.POST.get('card_18')
        card_19 = request.POST.get('card_19')
        card_20 = request.POST.get('card_20')
        card_21 = request.POST.get('card_21')
        card_22 = request.POST.get('card_22')
        card_23 = request.POST.get('card_23')
        card_24 = request.POST.get('card_24')
        card_25 = request.POST.get('card_25')
        card_26 = request.POST.get('card_26')
        card_27 = request.POST.get('card_27')
        card_28 = request.POST.get('card_28')
        card_29 = request.POST.get('card_29')
        card_30 = request.POST.get('card_30')
        card_31 = request.POST.get('card_31')
        card_32 = request.POST.get('card_32')
        card_33 = request.POST.get('card_33')
        x= [card_1,
            card_2,
            card_3,
            card_4,
            card_5,
            card_6,
            card_7, 
            card_8,
            card_9,
            card_10,
            card_11,
            card_12,
            card_13,
            card_14,
            card_15,
            card_16,
            card_17,
            card_18,
            card_19,
            card_20,
            card_21,
            card_22,
            card_23,
            card_24,
            card_25,
            card_26,
            card_27,
            card_28,
            card_29,
            card_30,
            card_31,
            card_32,
            card_33]
        for i in range(len(x)):
            print(i,'=',x[i])
            if x[i]=='on':
                x[i]=True
        card = CardioVasculaire(
            card_1 =x[0],
            card_2 =x[1],
            card_3 =x[2],
            card_4 =x[3],
            card_5 =x[4],
            card_6 =x[5],
            card_7 =x[6],
            card_8 =x[7],
            card_9 =x[8],
            card_10 =x[9],
            card_11 =x[10],
            card_12 =x[11],
            card_13 =x[12],
            card_14 =x[13],
            card_15 =x[14],
            card_16 =x[15],
            card_17 =x[16],
            card_18 =x[17],
            card_19 =x[18],
            card_20 =x[19],
            card_21 =x[20],
            card_22 =x[21],
            card_23 =x[22],
            card_24 =x[23],
            card_25 =x[24],
            card_26 =x[25],
            card_27 =x[26],
            card_28 =x[27],
            card_29 =x[28],
            card_30 =x[29],
            card_31 =x[30],
            card_32 =x[31],
            card_33 =x[32]
        )
        card.save()
        print('xx=',x)
        did = request.session['did']
        doss = Dossier.objects.get(pk=did)
        t = Form(cardio_vasculaireid=CardioVasculaire.objects.get(pk=card.pk))
        t.save()
        doss.formid = Form.objects.get(pk=t.pk)
        doss.save()
    return render(request, "accounts/patient_form.html")

@login_required
def patient_profile(request: HttpRequest) -> HttpResponse:
    ok = request.session['id']
    data = Patient.objects.get(id=ok)
    try:
        doss = Dossier.objects.all().filter(patientid=ok)
        print(doss)
    except:
        doss = {}
    try:
        phone = Phone.objects.all().filter(patientid=ok)
        print(phone[1].number)
    except:
        phone = {}
    
    if request.method == "POST" and 'run_script' in request.POST:
        print('py_script')
        ins = Dossier(patientid = Patient.objects.get(id=ok))
        ins.save();
        print('added')

    if request.method == "POST" and request.is_ajax():
        did = request.POST.get('text')
        print(request.POST)
        print(did)
        request.session['did'] = did
    
    context = {"patient" : data,"dossier":doss, "Phone":phone}
    return render(request, "accounts/patient_profile.html",context)

def patients(request: HttpRequest) -> HttpResponse:
    data = Patient.objects.all()
    context = {"Patient_number" : data}
    if request.method == "POST" and request.is_ajax():
        idd = request.POST.get('text')
        print(request.POST)
        print(idd)
        request.session['id'] = idd

    return render(request, "accounts/patients.html",context)

def dossier(request: HttpRequest):
    idd_doss = request.session['did']
    id_patient = request.session['id']
    dossier = Dossier.objects.get(id=idd_doss)
    data = Patient.objects.all().filter(id=id_patient)
    context = {'dossier':dossier,'patients':data}
    print('added')
    return render(request,"accounts/dossier.html",context)
