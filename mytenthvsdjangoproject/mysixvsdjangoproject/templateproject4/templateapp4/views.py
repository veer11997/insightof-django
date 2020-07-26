from django.shortcuts import render

import datetime
def homePageView(request):
    today=datetime.datetime.now()
    page='template Demo'
    context={'now':today,"name":page}
    return render(request,'templateapp4/showdatetime.html',context)
# Create your views here.
