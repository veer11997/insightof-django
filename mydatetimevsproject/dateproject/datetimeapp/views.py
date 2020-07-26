from django.shortcuts import render
from django.http import HttpResponse
import datetime

def dateView(request):
    today=datetime.datetime.now()
    datestr=today.strftime("%d-%b-%y")
    return HttpResponse("<h1>current date is :"+datestr+"</h1>")


def timeView(request):
    today=datetime.datetime.now()
    timestr=today.strftime("%H-%M-%S")
    return HttpResponse("<h1>current time is :"+timestr+"</h1>")
    




# Create your views here.
