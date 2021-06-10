from django.core.checks import messages
from django.views.generic.base import TemplateView
from django.views.generic import ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest, HttpResponse ,HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .forms import registerform
from .models import CardioVasculaire, Divers, Dossier, Enceinte, Encours, Form, Patient, Pediatriques, Phone, Pulmonaires, Renaux , Neurologiques, Hormonaux,Digestifs,Allergiques,Hematologiques,Rhumatologiques,Habitudes,Familiaux,Chirurgicaux,Operation,Dentaire,Gyneco, Traitement, pics
from .models import Pediatriques,Traitement,Encours,pics
from django.contrib.auth.decorators import login_required
import logging

class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = "accounts/profile.html"
    
logging.basicConfig(filename='static/test.txt', level=logging.DEBUG,format='%(funcName)s:%(message)s:%(asctime)s')
    

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            logging.debug(' {} :logged in'.format(user.username))
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
                inss = Phone(number=item,patientid=new)
                inss.save()
            message = 'Patient added succesufly ....!'
            context = { 'msg' : message }
            current_user = request.user
            logging.debug(' {}#{}:added:by:{}'.format(ins.name,ins.pk,current_user.username))
            return render(request, "accounts/register.html")
        else:
            context = {}
            return render(request, 'accounts/register.html', context)

@login_required
def patient_form(request: HttpRequest) -> HttpResponse:

    if request.method == 'POST':
        #verifer_pass
        user_object = request.user
        password = request.POST.get('password')
        
        if user_object.check_password(password) == False :
            logout(request)
            return render(request, "index.html")
            

        #I-cardio Vasculaire
        card_1 = request.POST.get('card_1')
        card_2 = request.POST.get('card_2')
        card_3 = request.POST.get('card_3')
        card_4 = request.POST.get('card_4')
        card_5 = request.POST.get('card_5')
        card_6 = request.POST.get('card_6')
        card_7 = request.POST.get('card_7')
        card_8 = request.POST.get('card_8')
        card_9 = request.POST.get('card_9')
        card_10 = request.POST.get('card_10')
        card_11 = request.POST.get('card_11')
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
        if(card_10 == 'on'):
            card_10 = request.POST.get('card_10_in')
        if(card_11 == 'on'):
            card_11 = str(request.POST.get('card_11_in'))
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
        if x[10] == 'None':
            x[10] = 'null'
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
        # II-pulmonaire
        pulm_1 = request.POST.get('pulm_1')
        pulm_2 = request.POST.get('pulm_2')
        pulm_3 = request.POST.get('pulm_3')
        pulm_4 = request.POST.get('pulm_4')
        pulm_5 = request.POST.get('pulm_5')
        pulm_6 = request.POST.get('pulm_6')
        pulm_7 = request.POST.get('pulm_7')
        pulm_8 = request.POST.get('pulm_8')
        pulm_9 = request.POST.get('pulm_9')
        pulm_10 = request.POST.get('pulm_10')
        pulm_11 = request.POST.get('pulm_11')
        pulm_12 = request.POST.get('pulm_12')
        pulm_13 = request.POST.get('pulm_13')
        pulm_14 = request.POST.get('pulm_14')
        x= [ pulm_1,pulm_2,pulm_3,pulm_4,pulm_5,pulm_6,pulm_7,pulm_8,pulm_9,pulm_10,pulm_11,pulm_12,pulm_13,pulm_14]
        for i in range(len(x)):
            print(i,'=',x[i])
            if x[i]=='on':
                x[i]=True
        pulm = Pulmonaires(pulm_1=x[0],pulm_2=x[1],pulm_3=x[2],pulm_4=x[3],pulm_5=x[4],pulm_6=x[5],pulm_7=x[6],pulm_8=x[7],pulm_9=x[8],pulm_10=x[9],pulm_11=x[10],pulm_12=x[11],pulm_13=x[12],pulm_14=x[13])
        pulm.save()
        # III-renaux
        renau_1 = request.POST.get('renau_1')
        renau_2 = request.POST.get('renau_2')
        renau_3 = request.POST.get('renau_3')
        renau_4 = request.POST.get('renau_4')
        renau_5 = request.POST.get('renau_5')
        renau_6 = request.POST.get('renau_6')
        x= [ renau_1,renau_2,renau_3,renau_4,renau_5,renau_6]
        for i in range(len(x)):
            print(i,'=',x[i])
            if x[i]=='on':
                x[i]=True
        renau = Renaux(renau_1=x[0],renau_2=x[1],renau_3=x[2],renau_4=x[3],renau_5=x[4],renau_6=x[5])
        renau.save()
        # III-Nerologique
        nero_1 = request.POST.get('nero_1')
        nero_2 = request.POST.get('nero_2')
        nero_3 = request.POST.get('nero_3')
        nero_4 = request.POST.get('nero_4')
        nero_5 = request.POST.get('nero_5')
        nero_6 = request.POST.get('nero_6')
        x= [ nero_1,nero_2,nero_3,nero_4,nero_5,nero_6]
        for i in range(len(x)):
            print(i,'=',x[i])
            if x[i]=='on':
                x[i]=True
        nero = Neurologiques(neuro_1=x[0],neuro_2=x[1],neuro_3=x[2],neuro_4=x[3],neuro_5=x[4],neuro_6=x[5])
        nero.save()
        # IV-Hormo
        horm_1 = request.POST.get('horm_1')
        horm_2 = request.POST.get('horm_2')
        horm_3 = request.POST.get('horm_3')
        horm_4 = request.POST.get('horm_4')
        x= [ horm_1,horm_2,horm_3,horm_4]
        for i in range(len(x)):
            print(i,'=',x[i])
            if x[i]=='on':
                x[i]=True
        horm = Hormonaux(horm_1=x[0],horm_2=x[1],horm_3=x[2],horm_4=x[3])
        horm.save()
        # V-digestif
        digest_1 = request.POST.get('digest_1')
        digest_2 = request.POST.get('digest_2')
        digest_3 = request.POST.get('digest_3')
        digest_4 = request.POST.get('digest_4')
        digest_5 = request.POST.get('digest_5')
        digest_6 = request.POST.get('digest_6')
        digest_7 = request.POST.get('digest_7')
        digest_8 = request.POST.get('digest_8')
        option_A = request.POST.getlist('hepatit')
        digest_9 = request.POST.get('digest_9')
        if digest_8 == 'on':
            digest_8 = option_A
        x= [ digest_1,digest_2,digest_3,digest_4,digest_5,digest_6,digest_7,digest_8,digest_9]
        for i in range(len(x)):
            print(i,'=',x[i])
            if x[i]=='on':
                x[i]=True
        digest = Digestifs(digest_1=x[0],digest_2=x[1],digest_3=x[2],digest_4=x[3],digest_5=x[4],digest_6=x[5],digest_7=x[6],digest_8=x[7],digest_9=x[8])
        digest.save()
        # VI-Allergique
        allerg_1 = request.POST.get('allerg_1')
        if allerg_1 == 'on':
            allerg_1 = request.POST.get('allerg_1_in')
        allerg_2 = request.POST.get('allerg_2')
        if allerg_2 == 'on':
            allerg_2 = request.POST.get('allerg_2_in')
        allerg_3 = request.POST.get('allerg_3')
        if allerg_3 == 'on':
            allerg_3 = request.POST.get('allerg_3_in')
        allerg_4 = request.POST.get('allerg_4')
        if allerg_4 == 'on':
            allerg_4 = request.POST.get('allerg_4_in')
        allerg_5 = request.POST.get('allerg_5')
        if allerg_5 == 'on':
            allerg_5 = request.POST.get('allerg_5_in')
        allerg_6 = request.POST.get('allerg_6')
        if allerg_6 == 'on':
            allerg_6 = request.POST.get('allerg_6_in')

        x= [ allerg_1,allerg_2,allerg_3,allerg_4,allerg_5,allerg_6]
        allerg = Allergiques(allerg_1=x[0],allerg_2=x[1],allerg_3=x[2],allerg_4=x[3],allerg_5=x[4],allerg_6=x[5])
        allerg.save()
        # VII-Hematologiques
        hemato_1 = request.POST.get('hemato_1')
        hemato_2 = request.POST.get('hemato_2')
        if hemato_2 == 'on':
            hemato_2 = request.POST.get('hemato_2_in')
        hemato_3 = request.POST.get('hemato_3')
        hemato_4 = request.POST.get('hemato_4')
        hemato_5 = request.POST.get('hemato_5')
        if hemato_5 == 'on':
            hemato_5 = request.POST.get('hemato_5_in')
        hemato_6 = request.POST.get('hemato_6')
        if hemato_6 == 'on':
            hemato_6 = request.POST.get('hemato_6_in')
        x= [ hemato_1,hemato_2,hemato_3,hemato_4,hemato_5,hemato_6]
        for i in range(len(x)):
            print(i,'=',x[i])
            if x[i]=='on':
                x[i]=True
        hemato = Hematologiques(hemato_1=x[0],hemato_2=x[1],hemato_3=x[2],hemato_4=x[3],hemato_5=x[4],hemato_6=x[5])
        hemato.save()
        # VIII-rhumatologiques
        rhumatol_1 = request.POST.get('rhumatol_1')
        rhumatol_2 = request.POST.get('rhumatol_2')
        rhumatol_3 = request.POST.get('rhumatol_3')
        rhumatol_4 = request.POST.get('rhumatol_4')
        if rhumatol_4 == 'on':
            rhumatol_4 = request.POST.get('rhumatol_4_in')
        rhumatol_5 = request.POST.get('rhumatol_5')
        x= [ rhumatol_1,rhumatol_2,rhumatol_3,rhumatol_4,rhumatol_5]
        for i in range(len(x)):
            print(i,'=',x[i])
            if x[i]=='on':
                x[i]=True
        rhumatol = Rhumatologiques(rhumatol_1=x[0],rhumatol_2=x[1],rhumatol_3=x[2],rhumatol_4=x[3],rhumatol_5=x[4])
        rhumatol.save()
        # VIII-Habitudes
        habit_1 = request.POST.get('habit_1')
        habit_2 = request.POST.get('habit_2')
        habit_3 = request.POST.get('habit_3')
        x= [ habit_1,'null',habit_2,habit_3]
        from .models import Fumer
        cigarette = request.POST.get('cigarette')
        chicha = request.POST.get('chicha')
        tabagisme = request.POST.get('tabagisme')
        fumer = Fumer(cigarette = cigarette,chicha = chicha,tabagisme = tabagisme)
        fumer.save()
        x[1]= Fumer.objects.get(pk=fumer.pk)
        for i in range(len(x)):
            print(i,'=',x[i])
            if x[i]=='on':
                x[i]=True
        habit = Habitudes(habit_1=x[0],fumerid=x[1],habit_2=x[2],habit_3=x[3])
        habit.save()
        # VII-Familiaux
        famil_1 = request.POST.get('famil_1')
        if famil_1 == 'on':
            famil_1 = request.POST.get('famil_1_in')
        famil_2 = request.POST.get('famil_2')
        famil_3 = request.POST.get('famil_3')
        if famil_3 == 'on':
            famil_3 = request.POST.get('famil_3_in')
        famil_4 = request.POST.get('famil_4')
        if famil_4 == 'on':
            famil_4 = request.POST.get('famil4_in')
        famil_5 = request.POST.get('famil_5')
        famil_6 = request.POST.get('famil_6')
        famil_7 = request.POST.get('famil_7')
        famil_8 = request.POST.get('famil_8')
        x= [ famil_1,famil_2,famil_3,famil_4,famil_5,famil_6,famil_7,famil_8]
        for i in range(len(x)):
            print(i,'=',x[i])
            if x[i]=='on':
                x[i]=True
        famil = Familiaux(famil_1=x[0],famil_2=x[1],famil_3=x[2],famil_4=x[3],famil_5=x[4],famil_6=x[5],famil_7=x[6],famil_8=x[7])
        famil.save()
        # VII-Churgiricqux
        churg_0 = request.POST.get('churg_0')
        churg_1 = request.POST.get('churg_1')
        if churg_1 == 'on':
            churg_1 = request.POST.get('churg_1_in')
        churg_2 = request.POST.get('churg_2')
        if churg_2 == 'on':
            churg_2 = request.POST.get('churg_2_in')
        x= [ churg_0,churg_1,churg_2]
        for i in range(len(x)):
            print(i,'=',x[i])
            if x[i]=='on':
                x[i]=True
        churg = Chirurgicaux(churg_0=x[0],churg_1=x[1],churg_2=x[2])
        churg.save()
        if Chirurgicaux.objects.filter(pk=churg.pk).exists():
            chirurgicauxid=Chirurgicaux.objects.get(pk=churg.pk)
        operation = request.POST.getlist('nature')
        date = request.POST.getlist('date')
        print(date)
        type = request.POST.getlist('type')
        for i in range(len(type)):
            if type[i] == '1':
                type[i] = 'Generale'
            if type[i] =='2':
                type[i] = 'Locorégionale axiale(Rachianesthésie, péridurale)'
            if type[i] =='3':
                type[i] = 'Locorégionale périphérique'
        print(type)
        for i in range(len(operation)):
            oper = Operation(nature=operation[i],dte=date[i],type=type[i],chirurgicauxid=chirurgicauxid)
            oper.save()

        # VII-dentaire
        dent_1 = request.POST.get('dent_1')
        if dent_1 == 'on':
            dent_1 = request.POST.get('dent_1_in')
        dent_2 = request.POST.get('dent_2')
        dent_3 = request.POST.get('dent_3')
        dent_4 = request.POST.get('dent_4')
        dent_5 = request.POST.get('dent_5')
        dent_6 = request.POST.get('dent_6')
        x= [ dent_1,dent_2,dent_3,dent_4,dent_5,dent_6]
        for i in range(len(x)):
            print(i,'=',x[i])
            if x[i]=='on':
                x[i]=True
        dent =Dentaire(dent_1=x[0],dent_2=x[1],dent_3=x[2],dent_4=x[3],dent_5=x[4],dent_6=x[5])
        dent.save()
        # VII-Divers
        dive_1 = request.POST.get('dive_1')
        dive_2 = request.POST.get('dive_2')
        dive_3 = request.POST.get('dive_3')
        dive_4 = request.POST.get('dive_4')
        if dive_4 == 'on':
            dive_4 = request.POST.get('dive_4_in')
        dive_5 = request.POST.get('dive_5')
        if dive_1 == 'on':
            dive_1 = request.POST.get('dive_5_in')
        dive_6 = request.POST.get('dive_6')
        if dive_3 == 'on':
            dive_3 = request.POST.get('dive_6_in')
        dive_7 = request.POST.get('dive_7')
        dive_8 = request.POST.get('dive_8')
        dive_9 = request.POST.get('dive_9')
        dive_10 = request.POST.get('dive_10')
        dive_11 = request.POST.get('dive_11')
        x= [ dive_1,dive_2,dive_3,dive_4,dive_5,dive_6,dive_7,dive_8,dive_9,dive_10,dive_11]
        for i in range(len(x)):
            print(i,'=',x[i])
            if x[i]=='on':
                x[i]=True
        dive = Divers(dive_1=x[0],dive_2=x[1],dive_3=x[2],dive_4=x[3],dive_5=x[4],dive_6=x[5],div_7=x[6],div_8=x[7],div_9=x[8],div_10=x[9],div_11=x[10])
        dive.save()
        # II-gyneco
        gyne_1 = request.POST.get('gyneco_1')
        gyne_2 = request.POST.get('gyneco_2')
        gyne_3 = request.POST.get('gyneco_3')
        if gyne_3 == 'on':
            gyne_3 = request.POST.get('gyneco_3_in')
        gyne_4 = request.POST.get('gyneco_4')
        gyne_5 = request.POST.get('gyneco_5')
        gyne_6 = request.POST.get('gyneco_6')
        gyne_7 = request.POST.get('gyneco_7')
        gyne_8 = request.POST.get('gyneco_8')
        gyne_9 = request.POST.get('gyneco_9')
        gyne_10 = request.POST.get('gyneco_10')
        gyne_11 = request.POST.get('gyneco_11')
        if gyne_11 == 'on':
            gyne_11 = request.POST.get('gyneco_11_in')
        gyne_12 = request.POST.get('gyneco_12')
        gyne_13 = request.POST.get('gyneco_13')
        gyne_14 = request.POST.get('gyneco_14')
        gyne_15 = request.POST.get('gyneco_15')
        gyne_16 = request.POST.get('gyneco_16')
        gyne_17 = request.POST.get('gyneco_17')
        gyne_18 = request.POST.get('gyneco_18')
        gyne_19 = request.POST.get('gyneco_19')
        x= [ gyne_1,gyne_2,gyne_3,gyne_4,gyne_5,gyne_6,gyne_7,gyne_8,gyne_9,gyne_10,gyne_11,gyne_12,gyne_13,gyne_14,gyne_15,gyne_16,gyne_17,gyne_18]
        for i in range(len(x)):
            if x[i]=='on':
                x[i]=True
        if gyne_19 == 'on':
            from .models import Enceinte
            a = request.POST.get('a')
            b = request.POST.get('b')
            c = request.POST.get('c')
            d = request.POST.get('d')
            e = request.POST.get('e')
            f = request.POST.get('f')
            g = request.POST.get('g')
            h = request.POST.get('h')
            if h == 'on':
                h = request.POST.get('h_in')
            i = request.POST.get('i')
            j = request.POST.get('j')
            x2 = [ a,b,c,d,e,f,g,h,i,j]
            for i in range(len(x2)):
                print(i,'=',x2[i])
                if x2[i]=='on':
                    x2[i]=True
            enceinte = Enceinte(a=x2[0],b=x2[1],c=x2[2],d=x2[3],e=x2[4],f=x2[5],g=x2[6],h=x2[7],i=x2[8],j=x2[9])
            enceinte.save()
            gyne = Gyneco(gyne_1=x[0],gyne_2=x[1],gyne_3=x[2],gyne_4=x[3],gyne_5=x[4],gyne_6=x[5],gyne_7=x[6],gyne_8=x[7],gyne_9=x[8],gyne_10=x[9],gyne_11=x[10],gyne_12=x[11],gyne_13=x[12],gyne_14=x[13],gyne_15=x[14],gyne_16=x[15],gyne_17=x[16],gyne_18=x[17],enceinteid=Enceinte.objects.get(pk=enceinte.pk))
            gyne.save()
        gyne = Gyneco(gyne_1=x[0],gyne_2=x[1],gyne_3=x[2],gyne_4=x[3],gyne_5=x[4],gyne_6=x[5],gyne_7=x[6],gyne_8=x[7],gyne_9=x[8],gyne_10=x[9],gyne_11=x[10],gyne_12=x[11],gyne_13=x[12],gyne_14=x[13],gyne_15=x[14],gyne_16=x[15],gyne_17=x[16],gyne_18=x[17])
        gyne.save()
        # II-gyneco
        pediatri_1 = request.POST.get('voix')
        pediatri_2 = request.POST.get('pediatri_2')
        pediatri_3 = request.POST.get('pediatri_3')
        pediatri_4 = request.POST.get('pediatri_4')
        pediatri_5 = request.POST.get('pediatri_5')
        pediatri_6 = request.POST.get('pediatri_6')
        if pediatri_6 == 'on':
            pediatri_6 = request.POST.get('pediatri_6_in')
        pediatri_7 = request.POST.get('pediatri_7')
        pediatri_8 = request.POST.get('pediatri_8')
        pediatri_9 = request.POST.get('pediatri_9')
        pediatri_10 = request.POST.get('pediatri_10')
        pediatri_11 = request.POST.get('pediatri_11')
        pediatri_12 = request.POST.get('pediatri_12')
        pediatri_13 = request.POST.get('pediatri_13')
        pediatri_14 = request.POST.get('pediatri_14')
        pediatri_15 = request.POST.get('pediatri_15')
        pediatri_16 = request.POST.get('pediatri_16')
        pediatri_17 = request.POST.get('pediatri_17')
        x= [ pediatri_1,pediatri_2,pediatri_3,pediatri_4,pediatri_5,pediatri_6,pediatri_7,pediatri_8,pediatri_9,pediatri_10,pediatri_11,pediatri_12,pediatri_13,pediatri_14,pediatri_15,pediatri_16,pediatri_17]
        pediatri = Pediatriques(pediatri_1=x[0],pediatri_2=x[1],pediatri_3=x[2],pediatri_4=x[3],pediatri_5=x[4],pediatri_6=x[5],pediatri_7=x[6],pediatri_8=x[7],pediatri_9=x[8],pediatri_10=x[9],pediatri_11=x[10],pediatri_12=x[11],pediatri_13=x[12],pediatri_14=x[13],pediatri_15=x[14],pediatri_16=x[15],pediatri_17=x[16])
        pediatri.save()
        # II-traitement
        meds = request.POST.getlist('meds')
        print('*********',meds)
        dose = request.POST.getlist('dose')
        print('*********',dose)
        matin = request.POST.getlist('matin')
        midi = request.POST.getlist('midi')
        soir = request.POST.getlist('soir')
        nuit = request.POST.getlist('nuit')
        if len(meds)>0:
            trait = Traitement()
            trait.save()
            for i in range(len(meds)):
                encours = Encours(meds=meds[i],dose=dose[i],matin=matin[i],midi=midi[i],soir=soir[i],nuit=nuit[i],traitementid=Traitement.objects.get(pk=trait.pk))
                encours.save()
        t = Form(
                    pulmonairesid=Pulmonaires.objects.get(pk=pulm.pk),
                    cardio_vasculaireid=CardioVasculaire.objects.get(pk=card.pk),
                    renauxid=Renaux.objects.get(pk=renau.pk),
                    neurologiquesid=Neurologiques.objects.get(pk=nero.pk),
                    hormonauxid=Hormonaux.objects.get(pk=horm.pk),
                    digestifsid=Digestifs.objects.get(pk=digest.pk),
                    allergiquesid=Allergiques.objects.get(pk=allerg.pk),
                    hematologiquesid=Hematologiques.objects.get(pk=hemato.pk),
                    rhumatologiquesid=Rhumatologiques.objects.get(pk=rhumatol.pk),
                    habitudesid = Habitudes.objects.get(pk=habit.pk),
                    familiauxid = Familiaux.objects.get(pk=famil.pk),
                    chirurgicauxid = Chirurgicaux.objects.get(pk=churg.pk),
                    dentaireid = Dentaire.objects.get(pk=dent.pk),
                    diversid = Divers.objects.get(pk=dive.pk),
                    gynecoid = Gyneco.objects.get(pk=gyne.pk),
                    pediatriquesid = Pediatriques.objects.get(pk=pediatri.pk)
                    )
        t.save()
        
        did = request.session['did']
        doss = Dossier.objects.get(pk=did)
        doss.formid = Form.objects.get(pk=t.pk)
        doss.save()
        current_user = request.user
        logging.debug(' form#{}:dossier#{}:added:by:{}'.format(t.pk,did,current_user.username))
    return render(request, "accounts/patient_form.html")

@login_required
def patient_profile(request: HttpRequest) -> HttpResponse:
    ok = request.session['id']
    current_user = request.user
    data = Patient.objects.get(id=ok)
    logging.debug(' {} :accesed:by:{}'.format(data.name,current_user.username))
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

#def media(request: HttpRequest):
#    doss_id = request.session['did']
#   return render(request,"accounts/patient_media.html")
class media(ListView):
    model = pics
    template_name = 'pics_list.html'
    def get_queryset(self):
        test_filter = self.request.session.get('did')
        return pics.objects.filter(dossierid=test_filter)

class addpicsView(CreateView):
    model = pics
    template_name = 'accounts/add_image.html'
    fields = ('discription','pic')
    def form_valid(self, form):
        form.instance.dossierid = Dossier.objects.get(pk=self.request.session.get('did'))
        return super(addpicsView, self).form_valid(form)