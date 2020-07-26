from django.shortcuts import render
import datetime

def dateView(request):

    today=datetime.datetime.now()
    curr_date=today.strftime('%d-%b-%Y')
    context={'date_str':curr_date}
    return render(request,'templateapp3/index.html',context)

def timeView(request):
    
    today=datetime.datetime.now()
    curr_time=today.strftime('%H-%M-%S')
    context={'time_str':curr_time}
    return render(request,'templateapp3/index.html',context)


# Create your views here.
