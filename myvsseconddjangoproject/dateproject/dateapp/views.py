from django.shortcuts import render
from django.http import HttpResponse
import datetime


# Create your views here.


def datePageView(request):
    today=datetime.datetime.now()
    str=today.strftime("%d-%b-%y")
    return HttpResponse("<h1>current date is "+str+"</h1>")
    