from django.http import HttpResponse,HttpRequest
from django.shortcuts import render, redirect

# from django.template import loader
def log(request: HttpRequest):
    
    return render(request,"admin/log.html")