from django.shortcuts import render


def homePageView(request):
    return render(request,'templatapp/index.html')
# Create your views here.
