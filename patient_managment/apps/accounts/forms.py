from django.forms import fields
from patient_managment.settings import POSTGRES_DB
from patient_managment.apps.accounts.models import Form
from django import forms
genre = ("homme","femme")
class registerform(forms.Form):
    name = forms.CharField(widget=forms.TextInput())
    age = forms.IntegerField(widget=forms.TextInput())
    sex = forms.ChoiceField(choices = genre)
    grade = forms.CharField(widget=forms.TextInput())
    mlle = forms.CharField(widget=forms.TextInput())
    profession = forms.CharField(widget=forms.TextInput())
    corps = forms.CharField(widget=forms.TextInput())
    family_stats = forms.CharField(widget=forms.TextInput())
    hospital_service = forms.CharField(widget=forms.TextInput())
    adresse = forms.CharField(widget=forms.TextInput())

